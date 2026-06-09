from typing import List
from neuronix.core.types import Document
from neuronix.core.logger import logger
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentSplitter:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
    def split_documents(self, documents: List[Document]) -> List[Document]:
        texts = [doc.page_content for doc in documents]
        metadatas = [doc.metadata for doc in documents]
        
        chunks = self.splitter.create_documents(texts, metadatas=metadatas)
        
        result = []
        for chunk in chunks:
            result.append(Document(page_content=chunk.page_content, metadata=chunk.metadata))
            
        logger.info(f"Split {len(documents)} documents into {len(result)} chunks")
        return result
