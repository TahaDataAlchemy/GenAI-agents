from data.schemaClass import State
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from api_client.api import llm


def entity_extraction_node_usecase(state: State):
    """
    Extract all the entities (Person, Organization, Location) from the text
    """
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma-separated list.\n\nText:{text}\n\nEntities:"
    )
    message = HumanMessage(content=prompt.format(text=state.text))  # Access state.text instead of state["text"]
    entities = llm.invoke([message]).content.strip().split(", ")  # Get a list of entities

    # Update the state with the extracted entities
    state.entities = entities

    return state  # Return the updated state with the entities
