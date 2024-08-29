from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"API KEY: {api_key[:6]}")
else:
    print("API KEY not found.")

document = SimpleDirectoryReader(r"LlamaOpenAI\NailProSupplyFAQ").load_data()

index  = VectorStoreIndex.from_documents(document)
engine = index.as_query_engine()
result = engine.query("Tell me about your Gel Nails")
print(result)

index.storage_context.persist("nail_index")