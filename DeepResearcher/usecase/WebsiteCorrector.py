from app.api_client.api import groq_client

def websiteNameCorrection(site: str) -> str:
    prompt = (
        f"You are an assistant that converts casual website names into their correct domain format.\n"
        f"For example:\n"
        f"Input: medium → Output: medium.com\n"
        f"Input: stackoverflow → Output: stackoverflow.com\n"
        f"Input: github → Output: github.com\n"
        f"Now convert the following:\n"
        f"{site}"
    )
    website = groq_client(prompt)
    return website.strip()
