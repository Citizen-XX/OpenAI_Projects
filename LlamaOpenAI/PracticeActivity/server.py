# %%
from fastapi import FastAPI
from pydantic import BaseModel
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.vector_stores import SimpleVectorStore

import uvicorn

# %%
app = FastAPI()

# %%
class Validator(BaseModel):
    text:str

# %%
storage_context = StorageContext.from_defaults(
    docstore=SimpleDocumentStore.from_persist_dir(
        persist_dir="LlamaOpenAI/ml_index"),
    vector_store=SimpleVectorStore.from_persist_dir(
        persist_dir="LlamaOpenAI/ml_index"),
    index_store=SimpleIndexStore.from_persist_dir(
        persist_dir="LlamaOpenAI/ml_index"),
)
#Alternatively we could just import the folder where all the index are stored
# storage_context = StorageContext.from_defaults(persist_dir="ml_index")
# %%
index = load_index_from_storage(storage_context)
engine = index.as_query_engine()

# %%
@app.get("/")
async def read_root():
    return {"message":"Server is Live"}

# %%
@app.post("/query_data")
async def querying(query:Validator):
    query_text = query.text
    result = engine.query(query_text)
    return {"result": result}

# %%
# The first parameter sent to the uvicorn.run method has to be the name of your
# server file withjout the ".py" and the variable name where you instanciated
# the FastAPI server
if __name__ == "__main__":
    uvicorn.run("server:app", host = "127.0.0.1", port = 8000, reload = True)