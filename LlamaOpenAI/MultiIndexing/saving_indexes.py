from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"API KEY: {api_key[:6]}")
else:
    print("API KEY not found.")

# Ensure the output directory exists
output_dir = r"LlamaOpenAI\V0_index"
os.makedirs(output_dir, exist_ok=True)

document_paths = [
    r"LlamaOpenAI\V0\Seguimiento SRMs Fondo de Innovacion.xlsx",
    r"LlamaOpenAI\V0\Template Solutioning KOF - DCC & Observability.pptx",
]
documents = []

for path in document_paths:
    try:
        doc = SimpleDirectoryReader(path).load_data()
        documents.extend(doc)
    except ValueError:
        print(f"Error loading file: {path}")

# Create the index from the multiple documents
index = VectorStoreIndex.from_documents(documents)

# Save the index to storage
storage_context = StorageContext.from_defaults(persist_dir=output_dir)
index.storage_context = storage_context
index.storage_context.persist()

# Load the index and create the query engine
storage_context = StorageContext.from_defaults(persist_dir=output_dir)
index = VectorStoreIndex.load_from_storage(storage_context)
engine = index.as_query_engine()
result = engine.query("Tell me about your Gel Nails")
print(result)