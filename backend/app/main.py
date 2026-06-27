from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from app.core.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Exoplanet Explorer API",
    description="Backend for analyzing and exploring exoplanetary data."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchQuery(BaseModel):
    method: Optional[str] = ""
    maxDistance: float
    minMass: float

@app.get("/")
def read_root():
    return {"message": "Hello Universe! The Exoplanet Analyst is online."}

@app.post("/api/exoplanets/search")
def search_exoplanets(query: SearchQuery):
    print(f"Incoming search scan: {query}")
    
    return {
        "status": "success",
        "message": "Deep space scan initiated.",
        "filters_received": query.model_dump(),
        "results": [] 
    }