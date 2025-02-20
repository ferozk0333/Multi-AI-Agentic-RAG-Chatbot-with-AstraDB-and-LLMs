from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

api_wrapper = WikipediaAPIWrapper(top_k_results = 1, doc_content_chars_max = 300)
wiki = WikipediaQueryRun(api_wrapper = api_wrapper)

## Define Functionality of Nodes

from typing import List

from typing_extensions import TypedDict

class GraphState(TypedDict):
  """
  Represents the state of our graph

  Attributes:
    question : question
    generation : LLM generation
    documents : list of documents
  """

  question = str                     # Question asked be user will be stored here
  generation = str
  documents: List[str]               # LLM Response will be stored here


  # For Vector DB Search Agent

def retrieve(state):
  """
  Retrieve Documents

  Args: 
    state (dict) : The current graph state

  Returns:
    state (dict) : New key added to state, documents, that contains retrived documents
  """

  print("---RETRIEVE---")
  question = state["question"]

  ## Retrieval
  documents = retriever.invoke(question)

  return {"documents":documents, "question":question}


# Similarly for Wikipedia Search Agent
from langchain.schema import Document

def wiki_search(state):
  """
  Wiki Search based on the re-phrased question.

  Args:
    state(dict) : The current state of the graph

  Returns:
    state(dict) : Updates document key with appended web results
  """

  print("---WIKIPEDIA---")
  question = state["question"]

  print(question)

  # Wiki Search
  # Doing wikipedia search, converting and returning them in documents
  docs = wiki.invoke({"query": question})
  wiki_results = docs
  wiki_results = Document(page_content = wiki_results)

  return {"documents": wiki_results, "question": question}

# Lastly, defining Routing node 

def route_question(state):
  """
  Route question to wiki search or RAG

  Args:
    state(dict) : The current graph state

  Returns:
    str: Next node to call
  """

  print("---ROUTE QUESTION---")
  question = state["question"]
  source = question_router.invoke({"question":question})

  if source.datasource == "wiki_search":
    return "wiki_search"
  elif source.datasource == "vectorstore":
    return "vectorstore"