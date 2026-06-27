from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.core.database import engine, get_db
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
def search_exoplanets(query: SearchQuery, db: Session = Depends(get_db)):

    db_query = db.query(models.Exoplanet)

    if query.method:
        db_query = db_query.filter(models.Exoplanet.discovery_method == query.method)
        
    db_query = db_query.filter(models.Exoplanet.distance_ly <= query.maxDistance)
    db_query = db_query.filter(models.Exoplanet.mass_earth >= query.minMass)
    
    results = db_query.all()
    
    return {
        "status": "success",
        "message": f"Deep space scan complete. Found {len(results)} planetary candidates.",
        "results": results
    }