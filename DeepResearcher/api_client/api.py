import os
import groq
from app.config import settings

# Set the environment variable for Groq API key
os.environ["GROQ_API_KEY"] = settings.GROQ_API_KEY

# Initialize Groq client
client = groq.Client()

# Use a powerful LLM
model_name = "llama3-70b-8192"

def groq_client(user_query: str, system_prompt: str = "You are a research assistant for DeepReacher. Provide concise, professional responses."):
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return response.choices[0].message.content.strip()
