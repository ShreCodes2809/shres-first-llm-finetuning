from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from colorama import Fore

if __name__ == "__main__":
    loader = PyPDFLoader("palantir_foundry_tech_doc.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = splitter.split_documents(docs)

    