from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import CharacterTextSplitter
from langchain_community import embeddings

def query_pdf(pdf_path: str, question: str) -> str:
    model_local = ChatOllama(model="llama3.2")
    docs = PyPDFLoader(pdf_path).load()
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text'),
    )
    retriever = vectorstore.as_retriever()

    rag_template = """Answer the question based only on the following context:
{context}
Question: {question}"""
    rag_prompt = ChatPromptTemplate.from_template(rag_template)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt
        | model_local
        | StrOutputParser()
    )

    return rag_chain.invoke(question)
