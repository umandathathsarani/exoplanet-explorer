from fastapi import FastAPI
from app.core.database import engine
from app.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Exoplanet Explorer API",
    description="Backend for analyzing and exploring exoplanetary data."
)

@app.get("/")
def read_root():
    return {"message": "Hello Universe! The Exoplanet Analyst is online."}