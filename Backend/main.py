from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()


DOCUMENT_PATH=os.environ['BOOK_PATH']

# Load the pdf
def load_document(DOCUMENT_PATH):
    loader = DirectoryLoader(
        path=DOCUMENT_PATH,
        glob='*.pdf',
        loader_cls=PyMuPDFLoader
    )
    return loader.lazy_load()

def create_chunks(loaded_document):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )
    text_chunk = text_splitter.split_documents(loaded_document)
    print('chunks created...')
    return text_chunk

MODEL_NAME= os.environ['EMB_MODEL']
def get_embedded_model():
    embedded_model = FastEmbedEmbeddings(
        model_name=MODEL_NAME
    )
    print('model created...')
    return embedded_model

def main():
    VECTOR_PATH = 'VECTOR'
    model = get_embedded_model()
    db = Chroma(
        collection_name="book_docs",
        embedding_function=model,
        persist_directory=VECTOR_PATH
    )

    batch_size = 8
    batch = []
    total = 0
    for document in load_document(DOCUMENT_PATH):
        batch.extend(create_chunks([document]))
        while len(batch) >= batch_size:
            db.add_documents(batch[:batch_size])
            total += batch_size
            batch = batch[batch_size:]
            print(f'Embedded {total} chunks...')


    if batch:
        db.add_documents(batch)
        total += len(batch)
        print(f'Embedded {total} chunks...')

    count = db._collection.count()
    print(f"Total documents inside ChromaDB: {count}")
    print('Everything done...')

if __name__ == '__main__':
    main()
