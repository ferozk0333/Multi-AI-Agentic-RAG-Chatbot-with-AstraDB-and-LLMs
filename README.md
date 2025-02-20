# Multi-AI-Agentic-RAG-Chatbot-with-AstraDB-and-LLMs

![Architecture Diagram] 
![image](https://github.com/user-attachments/assets/ad385764-1e89-4ffb-b027-6bbc80d1eff3)
 

## **Overview**  
This project implements a **multi-agent Retrieval-Augmented Generation (RAG) chatbot** using **LangGraph** and **AstraDB**. The chatbot routes user queries to either a **vector database** (AstraDB) for pre-stored knowledge retrieval or an **external search tool** (Wikipedia) based on query relevance. Large Language Models (LLMs) handle response generation, enabling dynamic and context-aware interactions.  

---

## **Key Features**  
1. Multi-agent AI chatbot with **LangGraph**  
2. Intelligent **query routing** using an LLM-based decision system  
3. **Prompt engineering** for refined chatbot responses  

---

## **Tech Stack**  
- **LangChain / LangGraph** – AI workflow orchestration  
- **AstraDB** – Vector database for knowledge retrieval  
- **Wikipedia API** – External knowledge source  
- **HuggingFace Embeddings** – Text embedding for document retrieval  
- **Groq LLM** – Query classification & response generation  

---

## **Project Workflow**  
1. **User Query Processing**  
   - The chatbot receives a question and routes it to either:  
     - **AstraDB** (Vector Database) for known information  
     - **Wikipedia API** for general queries  

2. **Data Retrieval & Response Generation**  
   - Vector searches using **HuggingFace embeddings**  
   - Wikipedia searches for real-time information  
   - LLM processes retrieved data and generates responses  

3. **Final Output**  
   - The chatbot returns an informative response to the user  

---




