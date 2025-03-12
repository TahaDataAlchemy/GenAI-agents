from langgraph.graph import StateGraph, END
from data.schemaClass import State
from usecase.classificationNode import classification_node_usecase
from usecase.entity_extractionNode import entity_extraction_node_usecase
from usecase.summarizationNode import summarization_node_usecase


def langgraphPipeline():
    workflow = StateGraph(State)
    # Add nodes to the graph
    workflow.add_node("classification_node", classification_node_usecase)
    workflow.add_node("entity_extraction", entity_extraction_node_usecase)
    workflow.add_node("summarization", summarization_node_usecase)

    # Add edges to the graph
    workflow.set_entry_point("classification_node") # Set the entry point of the graph
    workflow.add_edge("classification_node", "entity_extraction")
    workflow.add_edge("entity_extraction", "summarization")
    workflow.add_edge("summarization", END)

    # Compile the graph
    app = workflow.compile()

    return app

