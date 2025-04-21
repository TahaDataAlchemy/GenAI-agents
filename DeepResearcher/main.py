from app.usecase.search_usecase import duckduckgo_web_search
from app.usecase.GenerateRelatedQuestions import generate_related_questions
from app.usecase.SummarizationAgent import summarize_Search_agent
from app.usecase.WebsiteCorrector import websiteNameCorrection
from app.usecase.QueryDecomposer import query_decomposer
import sys
import os
import pprint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    """ Inputs """
    query = "How to deploy fastapi on AWS and tell me about AWS compatibility with deployment frameworks"
    
    link = None

    """Correcting the name of website if not written properly"""
    site = websiteNameCorrection(link)
    print(site)
    max_results = 1

    """Query Decomposition"""
    sub_queries = query_decomposer(query)
    print(f"Decomposed queries: {sub_queries}")


    """ Finding Query on Internet"""
    #appending result into dictionary so it can be summarized with key value pair 

    all_results = {}
    for sub_query in sub_queries:
        results = duckduckgo_web_search(sub_query, site,max_results)
        all_results[sub_query] = results 
        for idx, r in enumerate(results, 1):
            print(f"{idx}. {r['title']}")
            print(f"Link: {r['link']}")
            print(f"Snippet: {r['snippet']}\n")
            print(f"Full Text Preview:\n{r['full_text']}...\n{'-'*80}\n")
        
        """Generating Related Question"""
        related_Question = generate_related_questions(query)
        print(related_Question)

        print("_______________________________________________________________________________________________________________________________________________")

    
    """Agent for summarizing agent """
    pprint.pprint(all_results)
    Summary = summarize_Search_agent(all_results)
    print(Summary)
    print("\n")
