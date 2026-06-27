# Exoplanet Data Visualizer & Explorer 🪐

A full-stack web application that helps users navigate the vast catalog of discovered exoplanets, focusing on "habitable zone" candidates. 

## Features
* **Exoplanet Analyst:** Predicts the likelihood of liquid water or a habitable atmosphere based on theoretical planet conditions (e.g., star type, orbital distance).
* **NASA Data Integration:** Utilizes the NASA Exoplanet Archive (TAP service) as the primary data backbone.
* **Custom Research Workspaces:** Users can create comparison sets, save discovery papers, and write personal annotations on specific planetary findings.

## Tech Stack
* **Frontend:** Vue 3 (Composition API), Vite, Pinia (State Management)
* **Backend:** FastAPI (Python), SQLAlchemy (ORM), Pydantic (Data Validation)
* **Database:** PostgreSQL