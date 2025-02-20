from db_conn import db_connection

### Data Ingestion and Preprocessing
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Document URLs that we will read
urls = ['https://medium.com/analytics-vidhya/classification-in-machine-learning-ed30753d9461',
        'https://medium.com/@elisowski/ai-agents-vs-agentic-ai-whats-the-difference-and-why-does-it-matter-03159ee8c2b4',
        'https://skphd.medium.com/interview-questions-and-answers-on-retrieval-augmented-generation-rag-f5fb7b5b8228',
        'https://www.ibm.com/think/topics/langchain']

# Load the documents and then split the documents using Text Splitter
loader = WebBaseLoader(urls)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 600, chunk_overlap = 100)
texts = text_splitter.split_documents(docs)

# Let's convert the content into vector embeddings
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")

from langchain.vectorstores.cassandra import Cassandra
astra_vector_store = Cassandra(embedding=embeddings, 
                               table_name="qa_mini_demo1",
                               session = None,
                               keyspace=None)

# Insert documents into the vector DB
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
astra_vector_store.add_documents(texts)   # <- Insert all the documents

# This wrapper will allow us to interact with the database
astra_vector_index = VectorStoreIndexWrapper(vectorstore = astra_vector_store)

# Cannot directly use astra_vector_index to interact with database - Need a Retriever
retriever = astra_vector_store.as_retriever()

