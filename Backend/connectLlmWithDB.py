from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

GOOGLE_API_KEY = os.environ['API_KEY']

def laod_llm(GOOGLE_API_KEY):
    llm = ChatGoogleGenerativeAI(
        model='gemini-3.6-flash',
        temperature = 0.5,
        google_api_key = GOOGLE_API_KEY
    )
    return llm

TEMPLATE = """
You are a helpful and precise AI assistant.

Answer the user's question using ONLY the provided context.

Rules:
- If the answer is not contained in the context, say:
  "I cannot find the answer in the provided document."
- Keep the answer clear and factual.
- Do not make up facts.
- Do not use outside knowledge.

Context:
{context}

User Question:
{question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template=TEMPLATE)


EMBEDDING_MODEL = os.environ['EMB_MODEL']

embedding_model = FastEmbedEmbeddings(
    model = EMBEDDING_MODEL
)

VECTOR_PATH = 'VECTOR'

db = Chroma(
    collection_name = 'book_docs',
    embedding_function = embedding_model,
    persist_directory = VECTOR_PATH
)

retriever = db.as_retriever(
    search_kwargs= {
        'k' : 4
    }
)
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

llm = laod_llm(GOOGLE_API_KEY = GOOGLE_API_KEY)
qa_chain = (
    {
        'context': retriever,
        'question' : RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
print("\n--- RAG Bot Ready! Sawal pucho (Exit ke liye 'exit' likho) ---")
while True:
    query = input("\nSawal: ")
    if query.lower() in ['exit', 'quit']:
        break
    
    if not query.strip():
        continue
        
    response = qa_chain.invoke(query)
    print(response)

