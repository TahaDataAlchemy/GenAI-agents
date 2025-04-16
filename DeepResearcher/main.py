from app.usecase.search_usecase import duckduckgo_web_search
from app.usecase.GenerateRelatedQuestions import generate_related_questions
from app.usecase.SummarizationAgent import summarize_Search_agent
from app.usecase.WebsiteCorrector import websiteNameCorrection
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":
    """ Inputs """
    query = "How to deploy fastapi on AWS"
    link = "Wikipedia"

    #Correcting the name of website if not written properly
    site = websiteNameCorrection(link)
    print(site)
    max_results = 1

    """Generating Related Question"""
    
    related_Question = generate_related_questions(query)
    print(related_Question)

    """ Finding Query on Internet"""

    results = duckduckgo_web_search(query, site,max_results)
    for idx, r in enumerate(results, 1):
        print(f"{idx}. {r['title']}")
        print(f"Link: {r['link']}")
        print(f"Snippet: {r['snippet']}\n")
        print(f"Full Text Preview:\n{r['full_text']}...\n{'-'*80}\n")
    
    Summary = summarize_Search_agent(results)
    print(Summary)
    
