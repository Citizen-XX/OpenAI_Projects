from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
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

storage_context = StorageContext.from_defaults(persist_dir=r"LlamaOpenAI\nail_index")
index = load_index_from_storage(storage_context)
engine = index.as_query_engine()

app = FastAPI()

@app.get("/")
async def server_on():
    return {"message":"Nail Server Is On"}
@app.post("/ask")
async def query(query:Question):
    result = engine.query(query.question)
    return result

if __name__ == "__main__":
    uvicorn.run("server:app",host="127.0.0.1",port=8000, reload=True)