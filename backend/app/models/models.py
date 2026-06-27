from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    research_focus = Column(String, nullable=True)
    
    notes = relationship("PersonalNote", back_populates="researcher")

class StarSystem(Base):
    __tablename__ = "star_systems"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    temperature_k = Column(Float)
    luminosity = Column(Float)
    
    planets = relationship("Exoplanet", back_populates="host_star")

class Exoplanet(Base):
    __tablename__ = "exoplanets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    mass_earth = Column(Float)
    orbital_period_days = Column(Float)
    discovery_method = Column(String) # <-- NEW
    distance_ly = Column(Float)       # <-- NEW
    star_id = Column(Integer, ForeignKey("star_systems.id"))
    
    host_star = relationship("StarSystem", back_populates="planets")
    notes = relationship("PersonalNote", back_populates="planet")

class PersonalNote(Base):
    __tablename__ = "personal_notes"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    planet_id = Column(Integer, ForeignKey("exoplanets.id"))
    
    researcher = relationship("User", back_populates="notes")
    planet = relationship("Exoplanet", back_populates="notes")