"""LAYER Backend Application Entry Point."""

from fastapi import FastAPI

app = FastAPI(
    title="LAYER API",
    description="B2B 고신뢰성 문서 플랫폼 API",
    version="0.1.0",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy"}
