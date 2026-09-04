import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_community.vectorstores import FAISS

load_dotenv()

BOOK_DIRECTORY= os.environ['BOOK_PATH']   



def load_pdf_document(document_path : str) -> list:
    '''
    load the pdf file and then return the file

    @args : file path of the pdf file

    @return :  loaded file data
    '''
    # Initializing the pdf file
    loader = DirectoryLoader(path=document_path,
                             glob='*.pdf',
                             loader_cls=PyPDFLoader)
    #load the pdf file 
    file = loader.load()

    # Return the file data
    return file

def create_chunk(loaded_file):
    '''
    make the file data in chunk 

    @args : receive the load_pdf_data that are return the loaded data

    @retutn Return the data in chunks

    '''

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                   chunk_overlap=50)

    # make the data in chunks
    text_chunk = text_splitter.split_documents(loaded_file)

    #return the data in chunks
    return text_chunk


# google gemini api that are received from the .env file
GOOGLE_API_KEY= os.environ['API_KEY']

def embedding():
    '''
    create a model for the embedding 

    @return return the model
    '''

    # define the model 
    model = GoogleGenerativeAIEmbeddings(
        model='gemini-embedding-001',
        google_api_key=GOOGLE_API_KEY
    )
    # return the model 
    return model




def main():
    VECTORDB_PATH = 'vector/FAISS'
    loaded_document = load_pdf_document(BOOK_DIRECTORY)
    chunks_data = create_chunk(loaded_document)
    model = embedding()
    db = FAISS.from_documents(chunks_data, model)
    db.save_local(VECTORDB_PATH)

if __name__ == '__main__':
    main()
    print('saved successfully...')

