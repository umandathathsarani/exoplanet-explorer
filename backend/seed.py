from app.core.database import SessionLocal, engine
from app.models.models import Base, StarSystem, Exoplanet

print("Rebuilding database tables...")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

print("Injecting star systems...")
trappist = StarSystem(name="TRAPPIST-1", temperature_k=2566, luminosity=0.0005)
kepler = StarSystem(name="Kepler-186", temperature_k=3788, luminosity=0.05)
proxima = StarSystem(name="Proxima Centauri", temperature_k=3042, luminosity=0.0017)
kepler22 = StarSystem(name="Kepler-22", temperature_k=5518, luminosity=0.79)
lhs1140 = StarSystem(name="LHS 1140", temperature_k=3216, luminosity=0.0029)

db.add_all([trappist, kepler, proxima, kepler22, lhs1140])
db.commit()

print("Injecting exoplanets...")
planets = [
    Exoplanet(name="TRAPPIST-1 d", mass_earth=0.38, orbital_period_days=4.0, discovery_method="Transit", distance_ly=39.6, star_id=trappist.id),
    Exoplanet(name="TRAPPIST-1 e", mass_earth=0.69, orbital_period_days=6.1, discovery_method="Transit", distance_ly=39.6, star_id=trappist.id),
    Exoplanet(name="TRAPPIST-1 f", mass_earth=1.04, orbital_period_days=9.2, discovery_method="Transit", distance_ly=39.6, star_id=trappist.id),
    Exoplanet(name="Kepler-186 f", mass_earth=1.4, orbital_period_days=129.9, discovery_method="Transit", distance_ly=582, star_id=kepler.id),
    Exoplanet(name="Proxima Centauri b", mass_earth=1.27, orbital_period_days=11.2, discovery_method="Radial Velocity", distance_ly=4.2, star_id=proxima.id),
    Exoplanet(name="Kepler-22 b", mass_earth=36.0, orbital_period_days=289.9, discovery_method="Transit", distance_ly=620, star_id=kepler22.id),
    Exoplanet(name="LHS 1140 b", mass_earth=6.98, orbital_period_days=24.7, discovery_method="Transit", distance_ly=48.8, star_id=lhs1140.id)
]

db.add_all(planets)
db.commit()
db.close()

print("Database successfully seeded with expanded cosmic data!")