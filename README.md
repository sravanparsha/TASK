# Weather-PDF LangGraph AI Pipeline

This project demonstrates a **simple AI pipeline** using **LangChain**, **LangGraph**, **ChromaDB**, and **LangSmith**, with an interactive **Gradio UI**. It supports:

- Real-time weather queries via the **OpenWeatherMap API**  
- Question-answering over PDF documents using **RAG (Retrieval-Augmented Generation)**  
- Conditional routing of queries using **LangGraph nodes**  
- Evaluation of LLM responses using **LangSmith**  
- Testing critical components with **pytest**

---

## 🛠 Features

1. **Weather API Integration**
   - Fetch real-time weather data from OpenWeatherMap.
   - Parse city names from user queries.
   - Retry on API failures using `tenacity`.

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
