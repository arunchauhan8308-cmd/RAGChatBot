from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS

load_dotenv()

GOOGLE_API_KEY = os.environ['API_KEY']

def load_model(API_KEY):
    model = ChatGoogleGenerativeAI(
        model='gemini-3.6-flash',
        temprature=0.7,
        google_api_key=API_KEY
    )
    return model

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

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    api_key=GOOGLE_API_KEY
)


DOCUMENT_PATH = 'vector/FAISS'
db = FAISS.load_local(
    DOCUMENT_PATH,
    embedding_model,
    allow_dangerous_deserialization=True
)

retrivel_data = db.as_retriever(
    search_kwargs={
        'k':3
    }
)

llm = load_model(GOOGLE_API_KEY)
qa_chain = (
    {
        'context': retrivel_data,
        'question': RunnablePassthrough()
    }
    | prompt
    | llm
)

user_query = input('Write your query: ')
response = qa_chain.invoke(user_query)
print(response.content[0]['text'])

