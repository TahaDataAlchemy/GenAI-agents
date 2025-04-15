import traceback
from duckduckgo_search import DDGS
from typing import Optional, List
from app.usecase.parseSearch import extract_full_text
from app.data.dataModeling import SearchInput
from pydantic import ValidationError

def duckduckgo_web_search(query: str, site: Optional[str] = None, max_results: int = 10) -> List[dict]:
    try:
        # Validate inputs using the Pydantic model
        validated = SearchInput(query=query, site=site, max_results=max_results)
    except ValidationError as ve:
        raise ValueError(f"Input validation failed: {ve}")
    
    if not validated.query:
        raise ValueError("Query cannot be empty")

    search_query = f"site:{validated.site} {validated.query}" 
    if validated.site:
        search_query = f"site:{validated.site} {validated.query}"
    else:
        search_query = validated.query
    results = []

    with DDGS() as ddgs:
        for res in ddgs.text(search_query, region='wt-wt', safesearch="Moderate", max_results=validated.max_results):
            try:
                link = res.get("href", "No Link")
                full_text = extract_full_text(link) if link.startswith("http") else "No full text available"

                results.append({
                    "title": res.get("title", "No title"),
                    "link": link,
                    "snippet": res.get("body", "No snippet"),
                    "full_text": full_text
                })

            except Exception as e:
                error_trace = traceback.format_exc()
                results.append({
                    "title": res.get("title", "No title"),
                    "link": res.get("href", "No Link"),
                    "snippet": res.get("body", "No snippet"),
                    "full_text": f"Failed to extract full text: {e}\nTraceback:\n{error_trace}"
                })

    return results