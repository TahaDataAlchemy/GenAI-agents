from app.api_client.api import groq_client
import json
import re
import time
import logging

def query_decomposer(query: str) -> list:
    """
    Decomposes a complex query into sub-queries if needed using an LLM.
    Returns a list of sub-questions. If no decomposition is needed, returns the original query in a list.
    """

    QUERY_DECOMPOSITION_PROMPT = f"""
You are a smart query decomposition engine. Your job is to intelligently split a query into multiple sub-questions if the query includes multiple distinct intents or aspects.

### Guidelines:
- If it's a single query, return it as-is in a list.
- If the second question refers to the first, maintain full clarity.
- Improve clarity for better search, but do not change intent.
- Output only a JSON object with a `subQuestions` list.

### Examples:

#### Input:
"What is the best phone in 2024 and what are top laptops?"

#### Output:
{{
  "subQuestions": [
    "What is the best phone in 2024?",
    "What are the top laptops in 2024?"
  ]
}}

#### Input:
"What are the symptoms of flu?"

#### Output:
{{
  "subQuestions": [
    "What are the symptoms of flu?"
  ]
}}

### Input Query:
"{query}"

Now return only the JSON as described.
"""

    try:
        start_time = time.time()
        response = groq_client(QUERY_DECOMPOSITION_PROMPT)

        # Extract sub-questions
        pattern = r'"subQuestions"\s*:\s*\[(.*?)\]'
        match = re.search(pattern, response, re.DOTALL)

        if match:
            items = re.findall(r'"(.*?)"', match.group(1))
            questions = [item.strip() for item in items if item.strip()]
            logging.info(f"Query Decomposition took {time.time() - start_time:.2f} seconds")
            return questions if questions else [query]
        else:
            return [query]
    except Exception as e:
        logging.error(f"Query decomposition failed: {e}")
        return [query]
