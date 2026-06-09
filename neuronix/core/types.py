from pydantic import BaseModel, Field
from typing import Dict, Any

class Document(BaseModel):
    page_content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    
class QueryResult(BaseModel):
    answer: str
    source_documents: list[Document] = Field(default_factory=list)
