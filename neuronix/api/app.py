from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from neuronix.core.types import QueryResult
from neuronix.core.logger import logger

# Note: In a real app, you would initialize the pipeline globally 
# or via dependency injection. We provide a placeholder structure here.
app = FastAPI(title="Neuronix RAG API")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]

# Global pipeline instance to be set up at startup
pipeline = None

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    if pipeline is None:
        raise HTTPException(status_code=503, detail="RAG Pipeline is not initialized.")
        
    try:
        result = pipeline.query(request.query)
        sources = [{"content": doc.page_content, "metadata": doc.metadata} for doc in result.source_documents]
        return QueryResponse(answer=result.answer, sources=sources)
    except Exception as e:
        logger.error(f"API Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
        
@app.get("/health")
async def health_check():
    return {"status": "ok", "pipeline_initialized": pipeline is not None}
