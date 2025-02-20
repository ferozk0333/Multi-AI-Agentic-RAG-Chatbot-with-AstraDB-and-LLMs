# LangGraph Application
from typing import Literal

# When we are creating route query, we need to inherit the base model
# With function-calling models it's simple to use models for classification, which is what routing comes down to:
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field


# Data Model - this is all available in the documentation
class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "wiki_search"] = Field(
        ...,
        description="Given a user question choose which datasource would be most relevant for answering their question",
    )

from langchain_groq import ChatGroq
import os


GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize LLM Model
llm = ChatGroq(groq_api_key = GROQ_API_KEY, model_name = "llama-3.3-70b-versatile")

# Our router is very important, based on user query, I need to give control to either of the paths. 
# Let's integrate Route Query with LLM as well

structured_llm_router = llm.with_structured_output(RouteQuery)


# Let's create a prompt for router LLM
system = """You are an expert at routing a user question to the appropriate data source.

The vector store contains documents related to AI Agents, Basic Statistical Machine Learning Classification Algos(does not include Deep learning), RAG interview questions. 
Use the vector store for questions on these topics. Otherwise, use wiki search"""

route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

# Create a variable - this entire task will be done by our LLM
question_router = route_prompt | structured_llm_router   