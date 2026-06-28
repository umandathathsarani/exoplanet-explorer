from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from app.core.database import engine, get_db
from app.models import models
from google import genai
import os
import time
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.security import get_password_hash, verify_password, create_access_token
from jose import JWTError, jwt

load_dotenv()

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

class UserCreate(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")
oauth2_scheme_optional = OAuth2PasswordBearer(tokenUrl="api/auth/login", auto_error=False)

def get_optional_user(token: Optional[str] = Depends(oauth2_scheme_optional), db: Session = Depends(get_db)):
    if not token or token == "null":
        return None
    try:
        from app.core.security import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
    except JWTError:
        return None
        
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        from app.core.security import SECRET_KEY, ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

@app.post("/api/auth/register", response_model=Token)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
        
    hashed_password = get_password_hash(user.password)
    new_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/api/auth/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
        
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/")
def read_root():
    return {"message": "Hello Universe! The Exoplanet Analyst is online."}

@app.post("/api/exoplanets/search")
def search_exoplanets(query: SearchQuery, db: Session = Depends(get_db), current_user: Optional[models.User] = Depends(get_optional_user)):
    db_query = db.query(models.Exoplanet)
    if query.method:
        db_query = db_query.filter(models.Exoplanet.discovery_method == query.method)
    db_query = db_query.filter(models.Exoplanet.distance_ly <= query.maxDistance)
    db_query = db_query.filter(models.Exoplanet.mass_earth >= query.minMass)
    results = db_query.all()
    
    favorite_planet_ids = set()
    if current_user:
        favorites = db.query(models.UserFavorite).filter(models.UserFavorite.user_id == current_user.id).all()
        favorite_planet_ids = {fav.planet_id for fav in favorites}
        
    formatted_results = []
    for planet in results:
        planet_data = {
            "id": planet.id,
            "name": planet.name,
            "mass_earth": planet.mass_earth,
            "orbital_period_days": planet.orbital_period_days,
            "discovery_method": planet.discovery_method,
            "distance_ly": planet.distance_ly,
            "is_favorite": planet.id in favorite_planet_ids
        }
        formatted_results.append(planet_data)

    return {"status": "success", "message": f"Deep space scan complete. Found {len(results)} planetary candidates.", "results": formatted_results}

@app.get("/api/exoplanets/{planet_id}")
def get_planet_details(planet_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: 
        raise HTTPException(status_code=404, detail="Planet not found in database.")
    
    note = db.query(models.PersonalNote).filter(
        models.PersonalNote.planet_id == planet_id, 
        models.PersonalNote.user_id == current_user.id
    ).first()
    
    fav = db.query(models.UserFavorite).filter(
        models.UserFavorite.planet_id == planet_id, 
        models.UserFavorite.user_id == current_user.id
    ).first()
    
    host_star_data = {
        "name": planet.host_star.name if planet.host_star else "Unknown",
        "temperature_k": planet.host_star.temperature_k if planet.host_star else 0,
        "luminosity": planet.host_star.luminosity if planet.host_star else 0
    }
    
    return {
        "id": planet.id, "name": planet.name, "mass_earth": planet.mass_earth,
        "orbital_period_days": planet.orbital_period_days, "discovery_method": planet.discovery_method,
        "distance_ly": planet.distance_ly, "is_favorite": bool(fav),
        "note": note.content if note else "",
        "host_star": host_star_data
    }

@app.patch("/api/exoplanets/{planet_id}/favorite")
def toggle_favorite(planet_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")
    
    fav = db.query(models.UserFavorite).filter_by(user_id=current_user.id, planet_id=planet_id).first()
    if fav:
        db.delete(fav)
        is_fav = False
    else:
        new_fav = models.UserFavorite(user_id=current_user.id, planet_id=planet_id)
        db.add(new_fav)
        is_fav = True
        
    db.commit()
    return {"status": "success", "is_favorite": is_fav}

@app.post("/api/exoplanets/{planet_id}/note")
def save_research_note(planet_id: int, note_data: NoteUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")
    
    existing_note = db.query(models.PersonalNote).filter_by(planet_id=planet_id, user_id=current_user.id).first()
    
    if existing_note: 
        existing_note.content = note_data.content
    else: 
        db.add(models.PersonalNote(content=note_data.content, planet_id=planet_id, user_id=current_user.id))
        
    db.commit()
    return {"status": "success", "message": "Research log updated."}

@app.delete("/api/exoplanets/{planet_id}/note")
def delete_research_note(planet_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    note = db.query(models.PersonalNote).filter_by(planet_id=planet_id, user_id=current_user.id).first()
    if not note: raise HTTPException(status_code=404, detail="Note not found")
    
    db.delete(note)
    db.commit()
    return {"status": "success", "message": "Research log deleted."}

@app.post("/api/exoplanets/{planet_id}/analyze")
def get_ai_analysis(planet_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    planet = db.query(models.Exoplanet).filter(models.Exoplanet.id == planet_id).first()
    note = db.query(models.PersonalNote).filter_by(planet_id=planet_id, user_id=current_user.id).first()
    
    if not planet: raise HTTPException(status_code=404, detail="Planet not found")

    prompt = f"""
    Act as an astrophysicist. Provide a peer-review-style analysis for the exoplanet {planet.name}.
    
    Data:
    - Distance: {planet.distance_ly} light years
    - Mass: {planet.mass_earth} Earth masses
    - Orbital Period: {planet.orbital_period_days} days
    - Host Star: {planet.host_star.name} (Temperature: {planet.host_star.temperature_k}K, Luminosity: {planet.host_star.luminosity})
    - Researcher's Note: {note.content if note else 'None'}
    
    Analyze this planet's characteristics. Discuss its classification, potential composition, and habitability profile based on current astrophysical models. 
    Use precise, formal, and academic language appropriate for a professional research journal. 
    Conclude with a brief recommendation for future observational priority. Keep it under 150 words.
    """

    max_retries = 3
    wait_time = 2

    for i in range(max_retries):
        for key in API_KEYS:
            if not key.strip(): continue
            try:
                client = genai.Client(api_key=key.strip())
                response = client.models.generate_content(
                    model='gemini-2.0-flash', 
                    contents=prompt
                )
                return {"analysis": response.text}
            except Exception as e:
                print(f"Key failure: {e}")
                continue
        
        if i < max_retries - 1:
            time.sleep(wait_time)
            wait_time *= 2
        else:
            return {
                "analysis": f"[SIMULATED ACADEMIC REPORT] Exoplanet {planet.name} analysis remains consistent with standard astrophysical models. "
                            "High demand on computational resources currently prevents real-time generation. "
                            "Prioritize this system for future spectroscopic transit analysis."
            }

@app.get("/api/dashboard")
def get_user_dashboard(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    user_favorites = db.query(models.UserFavorite).filter(models.UserFavorite.user_id == current_user.id).all()
    favorite_planet_ids = [f.planet_id for f in user_favorites]
    
    favorite_planets = db.query(models.Exoplanet).filter(models.Exoplanet.id.in_(favorite_planet_ids)).all() if favorite_planet_ids else []
    
    formatted_favorites = []
    for planet in favorite_planets:
        formatted_favorites.append({
            "id": planet.id,
            "name": planet.name,
            "mass_earth": planet.mass_earth,
            "orbital_period_days": planet.orbital_period_days,
            "discovery_method": planet.discovery_method,
            "distance_ly": planet.distance_ly,
            "is_favorite": True
        })
        
    user_notes = db.query(models.PersonalNote).filter(models.PersonalNote.user_id == current_user.id).all()
    note_planet_ids = [n.planet_id for n in user_notes]
    note_planets = db.query(models.Exoplanet).filter(models.Exoplanet.id.in_(note_planet_ids)).all() if note_planet_ids else []
    
    planet_map = {p.id: p for p in note_planets}
    formatted_notes = []
    for note in user_notes:
        if note.planet_id in planet_map:
            p = planet_map[note.planet_id]
            formatted_notes.append({
                "id": p.id,
                "name": p.name,
                "mass_earth": p.mass_earth,
                "orbital_period_days": p.orbital_period_days,
                "discovery_method": p.discovery_method,
                "distance_ly": p.distance_ly,
                "is_favorite": p.id in favorite_planet_ids,
                "note_content": note.content
            })
            
    return {
        "status": "success",
        "favorites": formatted_favorites,
        "notes": formatted_notes
    }