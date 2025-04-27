from app.usecase.search_usecase import duckduckgo_web_search
from app.usecase.GenerateRelatedQuestions import generate_related_questions
from app.usecase.SummarizationAgent import summarize_Search_agent
from app.usecase.WebsiteCorrector import websiteNameCorrection
from app.usecase.QueryDecomposer import query_decomposer
from app.usecase.AgentMemory import AgentMemory
from app.usecase.ExtractReleventLink import extract_links_from_summary
import sys
import os
import pprint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == "__main__":

    memory = AgentMemory()
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
    related_questions_dict = {} 
    for sub_query in sub_queries:
        print(f"For {sub_query} results are")
        results = duckduckgo_web_search(sub_query, site,max_results)
        all_results[sub_query] = results # Using all_result dict because i wantt to save all the data in a format of key value pair so i can give it to summarizer agent   
        """Generating Related Question"""
        related_Question = generate_related_questions(query)
        print(related_Question)
        related_questions_dict[sub_query] = related_Question
    
        print("_______________________________________________________________________________________________________________________________________________")

    
    """Agent for summarizing agent """
    # pprint.pprint(all_results)

    Summary = summarize_Search_agent(all_results)
    print(Summary)
    links = extract_links_from_summary(Summary)

    for subquery,Elinks in zip(sub_queries,links):
        related_questions = related_questions_dict.get(subquery,[])
        memory.add(
            query=subquery,
            UserProvidedLink = link,
            related_questions = related_questions,
            relevent_link = Elinks,
            summary=Summary

        )
    print("\n")

