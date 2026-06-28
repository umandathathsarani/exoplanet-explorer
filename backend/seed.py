from sqlalchemy import text
from app.core.database import SessionLocal, engine
from app.models.models import Base, HostStar, Exoplanet

print("Rebuilding database tables...")

with engine.connect() as conn:
    conn.execute(text("DROP SCHEMA public CASCADE;"))
    conn.execute(text("CREATE SCHEMA public;"))
    conn.commit()

Base.metadata.create_all(bind=engine)

db = SessionLocal()

print("Injecting host stars...")
trappist = HostStar(name="TRAPPIST-1", temperature_k=2566, luminosity=0.0005)
kepler = HostStar(name="Kepler-186", temperature_k=3788, luminosity=0.05)
proxima = HostStar(name="Proxima Centauri", temperature_k=3042, luminosity=0.0017)
kepler22 = HostStar(name="Kepler-22", temperature_k=5518, luminosity=0.79)
lhs1140 = HostStar(name="LHS 1140", temperature_k=3216, luminosity=0.0029)

db.add_all([trappist, kepler, proxima, kepler22, lhs1140])
db.commit()

print("Injecting exoplanets...")
planets = [
    Exoplanet(name="TRAPPIST-1 d", mass_earth=0.38, orbital_period_days=4.0, discovery_method="Transit", distance_ly=39.6, host_star=trappist),
    Exoplanet(name="TRAPPIST-1 e", mass_earth=0.69, orbital_period_days=6.1, discovery_method="Transit", distance_ly=39.6, host_star=trappist),
    Exoplanet(name="TRAPPIST-1 f", mass_earth=1.04, orbital_period_days=9.2, discovery_method="Transit", distance_ly=39.6, host_star=trappist),
    Exoplanet(name="Kepler-186 f", mass_earth=1.4, orbital_period_days=129.9, discovery_method="Transit", distance_ly=582.0, host_star=kepler),
    Exoplanet(name="Proxima Centauri b", mass_earth=1.27, orbital_period_days=11.2, discovery_method="Radial Velocity", distance_ly=4.2, host_star=proxima),
    Exoplanet(name="Kepler-22 b", mass_earth=9.1, orbital_period_days=289.9, discovery_method="Transit", distance_ly=620.0, host_star=kepler22),
    Exoplanet(name="LHS 1140 b", mass_earth=6.6, orbital_period_days=24.7, discovery_method="Transit", distance_ly=41.0, host_star=lhs1140)
]

db.add_all(planets)
db.commit()

print("Database seeded successfully!")
db.close()