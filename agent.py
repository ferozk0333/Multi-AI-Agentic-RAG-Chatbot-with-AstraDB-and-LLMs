from langgraph.graph import START, END, StateGraph
workflow = StateGraph(GraphState)

# Define the nodes
workflow.add_node("wiki_search", wiki_search)   # Web Search -  Node name is "wiki_search", functionality is wiki_search
workflow.add_node("retrieve", retrieve)         # Do Vector Search

# Build the Graph
workflow.add_conditional_edges(
    START,
    route_question,
     {
        "wiki_search" : "wiki_search",
        "vectorstore" : "retrieve"
    }
)
workflow.add_edge("wiki_search", END)
workflow.add_edge("retrieve", END)

# Compile
app = workflow.compile()


# Refer to Documentation
from IPython.display import Image, display

try:
    display(Image(app.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass