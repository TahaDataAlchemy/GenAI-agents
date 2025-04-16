from app.api_client.api import groq_client
from typing import List

def generate_related_questions(main_query:str) -> List[str]:
    prompt = (
        f"Given the topic '{main_query}', generate 5 related, research-worthy questions "
        f"that a curious learner or researcher might ask. Keep them clear and relevant."
    )
    llm_Response = groq_client(prompt)
    return llm_Response