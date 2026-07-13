from fastapi import FastAPI

app = FastAPI(
    title="Travel Africa RAG Assistant",
    description="An AI-powered travel assistant that helps users discover hotels, explore destinations, and plan trips across Kenya and East Africa.",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Travel Africa RAG Assistant!"
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }
