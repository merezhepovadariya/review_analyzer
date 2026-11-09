from fastapi import FastAPI
from app.api.reviews import router as reviews_router

app = FastAPI(title="Review Analyzer")

app.include_router(reviews_router)
