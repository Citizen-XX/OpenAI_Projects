from pydantic import BaseModel
from llama_index.core import VectorStoreIndex, StorageContext, load_indices_from_storage
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
    persist_dir=r""
)

indices = load_indices_from_storage(storage_context)

engine = VectorStoreIndex.from_indices(indices).as_query_engine()

app = FastAPI()

@app.post("/answer")
def answer(question: Question):
    response = engine.query(question.question)
    return {"answer": response.response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)