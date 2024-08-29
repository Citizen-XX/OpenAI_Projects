# %%
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os
load_dotenv()

# %%
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"API KEY: {api_key[:6]}")
else:
    print("API KEY not found.")

documents = SimpleDirectoryReader("LlamaOpenAI\PDF").load_data()
# print(type(documents), len(documents))

# %%
# LlamaIndex has a built-in configuration system that automatically searches for the OPENAI_API_KEY in the environment variables when it initializes.
# If the environment variable doesn't exist that will create authentication errors when trying to query with the engine.
# If we do not wish to have the environment variable set in a .env file then we can also do: os.environ["OPENAI_API_KEY"] = "OurAPIKeyHere"
# Or we could set the key explicitly like: 
# from llama_index.llms import OpenAI
# from llama_index.core import Settings
# custom_api_key = os.getenv("OPENAI_API_KEY") or "OurAPIKeyHere"
# llm = OpenAI(api_key=custom_api_key)
# Settings.llm = llm

index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()
result = engine.query("What are the results of R over Python?")
print(result)

# %%
index.storage_context.persist("ml_index")
# %%
