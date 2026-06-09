from typing import List
from neuronix.embeddings.base import BaseEmbeddings
from neuronix.core.logger import logger
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

class BGEEmbeddings(BaseEmbeddings):
    def __init__(self, model_name: str = "BAAI/bge-small-en-v1.5"):
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        
        logger.info(f"Initializing BGE embeddings with model {model_name}")
        self.embeddings = HuggingFaceBgeEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self.embeddings.embed_documents(texts)
        
    def embed_query(self, text: str) -> List[float]:
        return self.embeddings.embed_query(text)