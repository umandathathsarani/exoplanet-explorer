import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db, get_current_user
from app.models.models import Base, User, Exoplanet, HostStar, PersonalNote
from app.core.security import get_password_hash
import json

# Setup in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

def override_get_current_user():
    return User(id=1, username="testuser", hashed_password="hashed_password")

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    
    # Create test data
    test_star = HostStar(id=1, name="TRAPPIST-1", temperature_k=2566, luminosity=0.0005)
    db.add(test_star)
    
    test_planet = Exoplanet(
        id=1,
        name="TRAPPIST-1 d",
        mass_earth=0.388,
        orbital_period_days=4.05,
        discovery_method="Transit",
        distance_ly=39.6,
        host_star_id=1
    )
    db.add(test_planet)
    
    test_note = PersonalNote(
        id=1,
        content="This is a test note for TRAPPIST-1 d.",
        user_id=1,
        planet_id=1
    )
    db.add(test_note)
    
    db.commit()
    yield
    Base.metadata.drop_all(bind=engine)

def test_analyze_endpoint_fallback(monkeypatch):
    # We want to test that the endpoint successfully fetches data from the DB 
    # and handles the fallback gracefully when no valid API key is present.
    
    # Mock os.getenv to return empty keys to force the fallback response
    monkeypatch.setattr("app.main.API_KEYS", [""])
    
    response = client.post("/api/exoplanets/1/analyze")
    assert response.status_code == 200
    
    data = response.json()
    assert "analysis" in data
    assert "SIMULATED ACADEMIC REPORT" in data["analysis"]
    assert "TRAPPIST-1 d" in data["analysis"]

def test_analyze_endpoint_not_found():
    response = client.post("/api/exoplanets/999/analyze")
    assert response.status_code == 404
    assert response.json()["detail"] == "Planet not found"
