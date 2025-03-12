from data.schemaClass import State
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from api_client.api import llm


def classification_node_usecase(state: State):
    """
    Classify the text into Categories: News, Blog, Research, or Other
    """
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Classify the following text into one of the categories: News, Blog, Research, or Other.\n\nText:{text}\n\nCategory:"
    )

    message = HumanMessage(content=prompt.format(text=state.text))
    classification = llm.invoke([message]).content.strip()

    # Update the state with the classification result
    state.classification = classification

    return state  # Return the updated state with the classification