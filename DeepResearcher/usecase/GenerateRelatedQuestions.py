from app.api_client.api import groq_client
from typing import List

def generate_related_questions(main_query: str) -> List[str]:
    prompt = (
        f"Given the topic '{main_query}', generate 5 short and clear related questions.\n"
        f"Only return the list of questions, without any explanation, reasoning, or extra text.\n"
        f"Format:\n"
        f"1. Question 1\n"
        f"2. Question 2\n"
        f"3. Question 3\n"
        f"4. Question 4\n"
        f"5. Question 5\n"
    )
    llm_Response = groq_client(prompt)
    return llm_Response
