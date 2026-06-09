from pathlib import Path
from typing import List
from neuronix.core.types import Document
from neuronix.core.logger import logger

class TextLoader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        
    def load(self) -> List[Document]:
        if not self.file_path.exists():
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")
            
        with open(self.file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        metadata = {"source": str(self.file_path)}
        logger.info(f"Loaded document from {self.file_path}")
        return [Document(page_content=content, metadata=metadata)]
