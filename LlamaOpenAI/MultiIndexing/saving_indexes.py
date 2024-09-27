import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"API KEY: {api_key[:6]}...")
else:
    print("API KEY not found.")

# Ensure the output directory for storing the index exists
output_dir = r"LlamaOpenAI\LLM_indexes"
os.makedirs(output_dir, exist_ok=True)

# Directory where your documents are located
docs_path = r"LlamaOpenAI\LLM_Docs"

# Load all documents recursively from the main directory using SimpleDirectoryReader
# SimpleDirectoryReader automatically handles loading files from subdirectories
documents = []
try:
    doc = SimpleDirectoryReader(docs_path, recursive=True).load_data()
    documents.extend(doc)
except ValueError as e:
    print(f"Error loading files from directory {docs_path}: {e}")

# Create an index from the loaded documents
index = VectorStoreIndex.from_documents(documents)

# Persist the index to disk (single folder with all necessary index data)
index.storage_context.persist(output_dir)

print(f"Index saved to {output_dir}")
