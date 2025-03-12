from data.schemaClass import State
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from api_client.api import llm


def summarization_node_usecase(state: State):
    """
    Summarize the text in one short sentence
    """
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text in one short sentence.\n\nText:{text}\n\nSummary:"
    )
    message = HumanMessage(content=prompt.format(text=state.text))  # Access state.text instead of state["text"]
    summary = llm.invoke([message]).content.strip()

    # Update the state with the summary
    state.summary = summary

    return state  # Return the updated state with the summary
