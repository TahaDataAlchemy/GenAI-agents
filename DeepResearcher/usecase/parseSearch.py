from typing import List
def parse_search_results(results_string: str) -> List[dict]:
    """Parse a string representation of search results into a list of dictionaries."""
    results = []
    entries = results_string.split(', snippet: ')
    for entry in entries[1:]:  # Skip the first split as it's empty
        parts = entry.split(', title: ')
        if len(parts) == 2:
            snippet = parts[0]
            title_link = parts[1].split(', link: ')
            if len(title_link) == 2:
                title, link = title_link
                results.append({
                    'snippet': snippet,
                    'title': title,
                    'link': link
                })
    return results