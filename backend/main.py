from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import math

app = FastAPI(title="Exoplanet Explorer API")

# Configure CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MOCK DATABASE ---
# In a real app, this would be SQLite, PostgreSQL, or a live NASA API wrapper.

mock_planets = [
    {
        "id": 1,
        "name": "Proxima Centauri b",
        "discovery_method": "Radial Velocity",
        "distance_ly": 4.24,
        "mass_earth": 1.17,
        "orbital_period_days": 11.2,
        "host_star": {"name": "Proxima Centauri", "temperature_k": 3042, "luminosity": "0.0017"},
        "is_favorite": False,
        "note": ""
    },
    {
        "id": 2,
        "name": "TRAPPIST-1e",
        "discovery_method": "Transit",
        "distance_ly": 39.46,
        "mass_earth": 0.69,
        "orbital_period_days": 6.1,
        "host_star": {"name": "TRAPPIST-1", "temperature_k": 2566, "luminosity": "0.0005"},
        "is_favorite": False,
        "note": ""
    },
    {
        "id": 3,
        "name": "Kepler-186f",
        "discovery_method": "Transit",
        "distance_ly": 582,
        "mass_earth": 1.44,
        "orbital_period_days": 129.9,
        "host_star": {"name": "Kepler-186", "temperature_k": 3788, "luminosity": "0.041"},
        "is_favorite": False,
        "note": ""
    },
    {
        "id": 4,
        "name": "51 Pegasi b",
        "discovery_method": "Radial Velocity",
        "distance_ly": 50.45,
        "mass_earth": 150.0,
        "orbital_period_days": 4.2,
        "host_star": {"name": "51 Pegasi", "temperature_k": 5793, "luminosity": "1.3"},
        "is_favorite": False,
        "note": ""
    },
    {
        "id": 5,
        "name": "HR 8799 c",
        "discovery_method": "Direct Imaging",
        "distance_ly": 129,
        "mass_earth": 2220, # roughly 7 Jupiter masses
        "orbital_period_days": 69000,
        "host_star": {"name": "HR 8799", "temperature_k": 7400, "luminosity": "4.9"},
        "is_favorite": False,
        "note": ""
    },
    {
        "id": 6,
        "name": "K2-18b",
        "discovery_method": "Transit",
        "distance_ly": 124,
        "mass_earth": 8.6,
        "orbital_period_days": 32.9,
        "host_star": {"name": "K2-18", "temperature_k": 3457, "luminosity": "0.023"},
        "is_favorite": False,
        "note": ""
    }
]

# --- MODELS ---
class LoginRequest(BaseModel):
    username: str
    password: str

class SearchFilters(BaseModel):
    method: str = ""
    maxDistance: float = 2000
    minMass: float = 0.1
    page: int = 1
    page_size: int = 20

class NoteRequest(BaseModel):
    content: str

# --- AUTH DEPENDENCY ---
def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return authorization.split(" ")[1]

# --- ENDPOINTS ---

@app.post("/api/auth/login")
def login(req: LoginRequest):
    # Dummy authentication that accepts anything
    if not req.username:
        raise HTTPException(status_code=400, detail="Username required")
    return {"access_token": f"mock_jwt_token_for_{req.username}"}

@app.post("/api/auth/register")
def register(req: LoginRequest):
    # Dummy registration that just logs in
    if not req.username:
        raise HTTPException(status_code=400, detail="Username required")
    return {"access_token": f"mock_jwt_token_for_{req.username}"}

@app.post("/api/exoplanets/search")
def search_exoplanets(filters: SearchFilters, token: str = Depends(verify_token)):
    results = mock_planets
    
    if filters.method:
        results = [p for p in results if p["discovery_method"].lower() == filters.method.lower()]
        
    results = [p for p in results if p["distance_ly"] <= filters.maxDistance]
    results = [p for p in results if p["mass_earth"] >= filters.minMass]
    
    total = len(results)
    
    # Pagination
    start_idx = (filters.page - 1) * filters.page_size
    end_idx = start_idx + filters.page_size
    paginated_results = results[start_idx:end_idx]
    
    return {
        "results": paginated_results,
        "total": total,
        "message": f"Scanned space and found {total} planetary bodies."
    }

@app.get("/api/exoplanets/{planet_id}")
def get_planet_details(planet_id: int, token: str = Depends(verify_token)):
    planet = next((p for p in mock_planets if p["id"] == planet_id), None)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    return planet

@app.patch("/api/exoplanets/{planet_id}/favorite")
def toggle_favorite(planet_id: int, token: str = Depends(verify_token)):
    planet = next((p for p in mock_planets if p["id"] == planet_id), None)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    planet["is_favorite"] = not planet["is_favorite"]
    return {"message": "Favorite status updated"}

@app.post("/api/exoplanets/{planet_id}/note")
def save_note(planet_id: int, req: NoteRequest, token: str = Depends(verify_token)):
    planet = next((p for p in mock_planets if p["id"] == planet_id), None)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    planet["note"] = req.content
    return {"message": "Note saved"}

@app.delete("/api/exoplanets/{planet_id}/note")
def delete_note(planet_id: int, token: str = Depends(verify_token)):
    planet = next((p for p in mock_planets if p["id"] == planet_id), None)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    planet["note"] = ""
    return {"message": "Note deleted"}

@app.post("/api/exoplanets/{planet_id}/analyze")
def analyze_planet(planet_id: int, token: str = Depends(verify_token)):
    planet = next((p for p in mock_planets if p["id"] == planet_id), None)
    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")
    
    # Dummy AI analysis
    analysis = f"Based on the spectral data of {planet['name']}, we observe an orbital period of {planet['orbital_period_days']} days. Orbiting {planet['host_star']['name']} at a distance of {planet['distance_ly']} LY, its mass of {planet['mass_earth']} Earth masses suggests intriguing geological structures. Conditions may be highly extreme."
    
    if planet["name"] == "TRAPPIST-1e":
        analysis += " This particular exoplanet lies within the habitable zone, making it a prime candidate for astrobiological research. Liquid water may exist on its surface."
        
    return {"analysis": analysis}

@app.get("/api/dashboard")
def get_dashboard(token: str = Depends(verify_token)):
    favorites = [p for p in mock_planets if p["is_favorite"]]
    notes = [
        {"id": p["id"], "name": p["name"], "note_content": p["note"]} 
        for p in mock_planets if p.get("note")
    ]
    return {"favorites": favorites, "notes": notes}
