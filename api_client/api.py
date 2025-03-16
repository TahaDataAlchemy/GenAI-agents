import os
from config import settings
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = settings.Groq_api_key 
def llm():
    llm = ChatGroq(
        model= "llama-3.3-70b-versatile",
        temperature=0 
    )
    return llm
llm=llm()