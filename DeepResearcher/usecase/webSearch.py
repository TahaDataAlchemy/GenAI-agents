from langchain_community.tools import DuckDuckGoSearchResults
from typing import Optional,List,Tuple
from parseSearch import parse_search_results

search = DuckDuckGoSearchResults()
print("Taha")
def perform_search(query: str,site:Optional[str] = None) -> Tuple[List[str],List[Tuple[str,str]]]:
    """ Perform a web search based on a query, optionally including a specific website """
    try:
        if site:
            specific_query = f"site: {site} {query}"
            print(f"Searching for: {specific_query}")
            specific_results = search.run(specific_query)
            print(f"Specific search results: {specific_results}")
            specific_parsed = parse_search_results(specific_results)

            general_query = f"-site:{site} {query}"
            print(f"Searching for: {general_query}")
            general_results = search.run(general_query)
            print(f"General search results: {general_results}")
            general_parsed = parse_search_results(general_results)
            combined_results = (specific_parsed + general_parsed)[:3]
        else:
            print(f"Searching for: {query}")
            web_results = search.run(query)
            print(f"Web results: {web_results}")
            combined_results = parse_search_results(web_results)[:3]
        
        web_knowledge = [result.get('snippet',"") for result in combined_results]
        sources = [(result.get('title', 'Untitled'), result.get('link', '')) for result in combined_results]
        print(f"Processed web_knowledge: {web_knowledge}")
        print(f"Processed sources: {sources}")
        return web_knowledge, sources
    except Exception as e:
        print(f"Error in perform_web_search: {str(e)}")
        import traceback
        traceback.print_exc()
        return [],[]

perform_search("Python programming", "wikipedia.org")