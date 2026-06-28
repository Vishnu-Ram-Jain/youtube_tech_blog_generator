import os
from dotenv import load_dotenv
from crewai import LLM
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv()

try:
    import crewai.llms.cache as _crewai_cache
    _crewai_cache.mark_cache_breakpoint = lambda msg: msg
except Exception:
    pass

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

settings = Settings()
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.2
)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    model_kwargs={"device": "cpu"}
)