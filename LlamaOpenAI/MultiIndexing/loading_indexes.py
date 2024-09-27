from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from fastapi import FastAPI
from dotenv import load_dotenv

import uvicorn
import os

load_dotenv()

class Question(BaseModel):
    question:str

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"API KEY: {api_key[:6]}")
else:
    print("API KEY not found.")

# Load multiple indexes from storage
storage_context = StorageContext.from_defaults(
    persist_dir=r"LlamaOpenAI\LLM_indexes"
)

indices = load_index_from_storage(storage_context)
engine = indices.as_query_engine()
# engine = VectorStoreIndex.from_indices(indices).as_query_engine()

app = FastAPI()

@app.get("/")
async def server_on():
    return {"message":"KOF Server is ON"}
@app.post("/ask")
async def query(query:Question):
    result = engine.query(query.question)
    return result

if __name__ == "__main__":
    uvicorn.run("loading_indexes:app", host="127.0.0.1", port=8000,reload=True)