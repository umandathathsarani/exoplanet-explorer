from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    notes = relationship("PersonalNote", back_populates="owner")
    favorites = relationship("UserFavorite", back_populates="user")

class Exoplanet(Base):
    __tablename__ = "exoplanets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    mass_earth = Column(Float)
    orbital_period_days = Column(Float)
    discovery_method = Column(String)
    distance_ly = Column(Float)
    
    host_star = relationship("HostStar", back_populates="planet", uselist=False)
    notes = relationship("PersonalNote", back_populates="planet")
    favorited_by = relationship("UserFavorite", back_populates="planet")

class HostStar(Base):
    __tablename__ = "host_stars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    temperature_k = Column(Float)
    luminosity = Column(Float)
    planet_id = Column(Integer, ForeignKey("exoplanets.id"))

    planet = relationship("Exoplanet", back_populates="host_star")

class PersonalNote(Base):
    __tablename__ = "personal_notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    planet_id = Column(Integer, ForeignKey("exoplanets.id"))
    user_id = Column(Integer, ForeignKey("users.id")) 

    planet = relationship("Exoplanet", back_populates="notes")
    owner = relationship("User", back_populates="notes")

class UserFavorite(Base):
    __tablename__ = "user_favorites"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    planet_id = Column(Integer, ForeignKey("exoplanets.id"))
    
    user = relationship("User", back_populates="favorites")
    planet = relationship("Exoplanet", back_populates="favorited_by")