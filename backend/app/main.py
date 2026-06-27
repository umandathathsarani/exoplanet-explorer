from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.core.database import engine, get_db
from app.models import models
from google import genai
import os

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

API_KEYS = os.getenv("GEMINI_API_KEYS", "").split(",")

class SearchQuery(BaseModel):
    method: Optional[str] = ""
    maxDistance: float
    minMass: float

class NoteUpdate(BaseModel):
    content: str

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
    return {"status": "success", "message": f"Found {len(results)} planetary candidates.", "results": results}

@app.get("/api/exoplanets/{planet_id}")
def get_planet_details(planet_id: int, db: Session = Depends(get_db)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found.")
    note = db.query(models.PersonalNote).filter(models.PersonalNote.planet_id == planet_id).first()
    return {
        "id": planet.id, "name": planet.name, "mass_earth": planet.mass_earth,
        "orbital_period_days": planet.orbital_period_days, "discovery_method": planet.discovery_method,
        "distance_ly": planet.distance_ly, "is_favorite": planet.is_favorite,
        "note": note.content if note else "",
        "host_star": {"name": planet.host_star.name, "temperature_k": planet.host_star.temperature_k, "luminosity": planet.host_star.luminosity}
    }

@app.patch("/api/exoplanets/{planet_id}/favorite")
def toggle_favorite(planet_id: int, db: Session = Depends(get_db)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")
    planet.is_favorite = not planet.is_favorite
    db.commit()
    return {"status": "success", "is_favorite": planet.is_favorite}

@app.post("/api/exoplanets/{planet_id}/note")
def save_research_note(planet_id: int, note_data: NoteUpdate, db: Session = Depends(get_db)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")
    existing_note = db.query(models.PersonalNote).filter(models.PersonalNote.planet_id == planet_id).first()
    if existing_note: existing_note.content = note_data.content
    else: db.add(models.PersonalNote(content=note_data.content, planet_id=planet_id))
    db.commit()
    return {"status": "success", "message": "Research log updated."}

@app.delete("/api/exoplanets/{planet_id}/note")
def delete_research_note(planet_id: int, db: Session = Depends(get_db)):
    note = db.query(models.PersonalNote).filter(models.PersonalNote.planet_id == planet_id).first()
    if not note: raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note); db.commit()
    return {"status": "success", "message": "Research log deleted."}

@app.post("/api/exoplanets/{planet_id}/analyze")
def get_ai_analysis(planet_id: int, db: Session = Depends(get_db)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    note = db.query(models.PersonalNote).filter(models.PersonalNote.planet_id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")

    prompt = f"""
    Act as an astrophysicist. Provide a peer-review-style analysis for {planet.name}.
    Data: Mass: {planet.mass_earth} M⊕, Period: {planet.orbital_period_days} days.
    Host Star: {planet.host_star.name}, Temp: {planet.host_star.temperature_k}K.
    Researcher's Note: {note.content if note else 'None'}
    
    Provide a formal, academic analysis regarding habitability potential. Keep under 150 words.
    """

    for key in API_KEYS:
        if not key.strip(): continue
        try:
            client = genai.Client(api_key=key.strip())
            response = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
            return {"analysis": response.text}
        except Exception as e:
            print(f"Key failed, trying next. Error: {e}")
            continue

    return {
        "analysis": f"[SIMULATED ACADEMIC REPORT] Exoplanet {planet.name} analysis remains consistent with current planetary models. "
                    f"Mass {planet.mass_earth} M⊕ suggests a potentially terrestrial core. "
                    "Continued observation is recommended to verify atmospheric signatures."
    }