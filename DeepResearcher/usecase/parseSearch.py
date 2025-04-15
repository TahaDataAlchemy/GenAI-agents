import requests
from bs4 import BeautifulSoup
import traceback
def extract_full_text(url: str) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove scripts/styles
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract main text
        paragraphs = soup.find_all("p")
        return "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
    except Exception as e:
        error_details = traceback.format_exc()
        return f"Failed to extract text: {e}\nTraceback:\n{error_details}"