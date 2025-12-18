# Weather-PDF LangGraph AI Pipeline

This project demonstrates a **simple AI pipeline** using **LangChain**, **LangGraph**, **ChromaDB**(similar to Qdrant), and **LangSmith**, with an interactive **Gradio UI**(similar to streamlit) using OLLAMA LLM. It supports:

- Real-time weather queries via the **OpenWeatherMap API**  
- Question-answering over PDF documents using **RAG (Retrieval-Augmented Generation)**  
- Conditional routing of queries using **LangGraph nodes**  
- Evaluation of LLM responses using **LangSmith**  
- Testing critical components with **pytest**

---
chatbot answers based on user question whether it is related to weather or from pdf uploaded
example1:(user question based on weather)
<img width="1920" height="1080" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/4d132754-4ab7-4e4b-a3e7-ec94b31e0f1b" />

example2:(user question based on pdf(example:constitution of india.pdf)
<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/251393b8-f6d9-4432-9d50-97a5d3d89898" />

## 🛠 Features

1. **Weather API Integration**
   - Fetch real-time weather data from OpenWeatherMap.
   - Parse city names from user queries.

2. **PDF RAG**
   - Load PDF documents and split text into chunks.
   - Generate embeddings using `OllamaEmbeddings`.
   - Store embeddings in **ChromaDB** vector database.
   - Retrieve relevant context for user questions.

3. **LangGraph Routing**
   - Conditional node execution:
     - Weather-related questions → Weather API node.
     - Other questions → PDF RAG node.
   - Modular and extensible pipeline.

4. **LangSmith Integration**
   - Tracks all LLM interactions.
   - Evaluates LLM responses and prompts.
   - Helps improve model performance and retrieval quality.

5. **Gradio Interface**
   - Upload PDFs and ask questions via a web-based UI.
   - Answers displayed in a user-friendly format.

---

## 📂 Project Structure

TASK/
│
├─ app.py # Gradio interface
├─ flow.py # LangGraph nodes and pipeline
├─ weather.py # Weather API integration
├─ rag_pdf.py # PDF RAG and ChromaDB
├─ is_weather_question.py # Weather question classifier
├─ tests/ # Unit tests
│ ├─ test_graph_routing.py
│ ├─ test_is_weather_question.py
│ └─ test_weather_api.py
└─ README.md

🔹 LangSmith Evaluation

LLM responses are automatically logged in LangSmith.
<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/a506bf8f-ac16-44a1-a2af-d8922e946e7d" />

<img width="1920" height="1080" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/5e732163-41dc-4798-9a87-4748c36c942d" />


