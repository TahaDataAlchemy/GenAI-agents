from app.api_client.api import groq_client
import json

def summarize_Search_agent(results: list[dict]) -> str:
    results_json = json.dumps(results, indent=2)

    prompt = (
        "You are an AI assistant. Summarize the following search results.\n"
        "Each item contains a title, snippet, link, and full text.\n\n"
        "Your task:\n"
        "- Provide a clear, concise summary of the most relevant content.\n"
        "- Highlight key steps or processes if instructions are involved.\n"
        "- Present the information in bullet points for readability.\n"
        "- At the end, recommend the most relevant link.\n"
        "- If an error is encountered (e.g., empty content or missing data), return only: 404\n\n"
        f"{results_json}"
    )

    summary = groq_client(prompt)
    return summary
