from fastapi import FastAPI

app = FastAPI(
    title="Exoplanet Explorer API",
    description="Backend for analyzing and exploring exoplanetary data."
)

@app.get("/")
def read_root():
    return {"message": "Hello Universe! The Exoplanet Analyst is online."}