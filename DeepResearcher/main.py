from app.usecase.search_usecase import duckduckgo_web_search
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    query = "python"
    site = "youtube.com"

    results = duckduckgo_web_search(query, site)
    for idx, r in enumerate(results, 1):
        print(f"{idx}. {r['title']}")
        print(f"Link: {r['link']}")
        print(f"Snippet: {r['snippet']}\n")
        print(f"Full Text Preview:\n{r['full_text']}...\n{'-'*80}\n")