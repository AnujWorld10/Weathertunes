from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Mood-based Song Recommender")
app.include_router(router)
