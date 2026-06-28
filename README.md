<div align="center">
  <img src="frontend/public/favicon.png" alt="Exoplanet Explorer Logo" width="120" />
  
  # Exoplanet Explorer
  
  **A breathtaking, interactive full-stack web application dedicated to the discovery, classification, and science of planets beyond our Solar System.**

  <!-- Badges -->
  <p align="center">
    <!-- Frameworks -->
    <img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D" alt="Vue.js" />
    <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
    <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <!-- Database & AI -->
    <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
    <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white" alt="Gemini AI" />
    <!-- Status -->
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="License: MIT" />
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome" />
  </p>

  <p align="center">
    <a href="https://linkedin.com/in/umandathathsarani"><b>LinkedIn</b></a> •
    <a href="https://github.com/umandathathsarani"><b>GitHub</b></a> •
    <a href="https://instagram.com/u_m_a_n_d_a_"><b>Instagram</b></a>
  </p>
</div>

<br/>

<details>
  <summary><b>Table of Contents</b></summary>
  <ul>
    <li><a href="#-about-the-project">About the Project</a></li>
    <li><a href="#-features">Features</a></li>
    <li><a href="#-project-architecture">Project Architecture</a></li>
    <li><a href="#-tech-stack">Tech Stack</a></li>
    <li><a href="#-getting-started">Getting Started</a></li>
    <li><a href="#-api-endpoints">API Endpoints</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
  </ul>
</details>

---

## 🌌 About the Project

**Exoplanet Explorer** is an educational and analytical platform designed for astronomy enthusiasts and researchers alike. It combines an immersive, responsive frontend UI built with Vue 3 with a robust, high-performance Python FastAPI backend. The platform provides interactive lessons, celestial quizzes, a live database search of exoplanets powered by PostgreSQL, and cutting-edge astrophysics analysis driven by Google's Gemini 2.0 AI.

## ✨ Features

- 📖 **Interactive Astronomy Lessons**: 10 comprehensive chapters covering everything from the Habitable Zone to Spectral Analysis.
- 🧠 **Dynamic Quizzes**: Test your knowledge across multiple difficulty tiers.
- 🔭 **Cosmic Query Search Engine**: Query a live PostgreSQL database of exoplanets filtered by mass, distance, and discovery method.
- 📡 **Personal Observatory Dashboard**: Create an account, bookmark your favorite exoplanets, and write secure, encrypted research notes.
- 🤖 **AI Astrobiology Analysis**: Utilize Google Gemini AI to generate peer-review style analysis of planetary viability and geological structures.
- 🌙 **Immersive UI/UX**: Dark mode by default, glassmorphism aesthetics, dynamic animations, and responsive layout.

---

## 📸 Screenshots

<div align="center">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182754.png" width="48%" alt="App Screenshot 1">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182810.png" width="48%" alt="App Screenshot 2">
  <br/>
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182834.png" width="48%" alt="App Screenshot 3">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182849.png" width="48%" alt="App Screenshot 4">
</div>

---

## 🏗️ Project Architecture

Exoplanet Explorer is a full-stack application. The repository is cleanly separated into client and server environments.

```text
exoplanet-explorer/
├── backend/                    # Python FastAPI Server & Database
│   ├── app/
│   │   ├── api/                # API route definitions
│   │   ├── core/               # Database connection, JWT Security, Config
│   │   ├── models/             # SQLAlchemy ORM Models (User, Exoplanet, Note)
│   │   ├── schemas/            # Pydantic validation schemas
│   │   └── main.py             # Server entrypoint & Gemini AI logic
│   └── .env                    # Environment variables (Neon DB, Gemini Keys)
├── frontend/                   # Vue 3 SPA Client
│   ├── public/                 # Static assets (favicons, background images)
│   └── src/
│       ├── assets/             # Logos and SVGs
│       ├── components/         # Reusable Vue Components (Modals, Cards)
│       ├── App.vue             # Root component and router logic
│       ├── main.js             # Vue mounting & Tailwind injection
│       └── style.css           # Global typography and base styles
```

---

## 💻 Tech Stack

### Frontend Client
- **Framework**: Vue 3 (Composition API)
- **Styling**: TailwindCSS 3
- **Build Tool**: Vite
- **Assets**: Heroicons & Custom SVG Animations

### Backend API
- **Framework**: Python FastAPI
- **Database Engine**: PostgreSQL (Hosted on Neon)
- **ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens) & Passlib (Bcrypt)
- **AI Integration**: Google Gemini 2.0 Flash SDK

---

## 🚀 Getting Started

Follow these steps to set up the full-stack environment on your local machine.

### Prerequisites
- Node.js (v18+)
- Python (3.10+)
- PostgreSQL Database (Local or Cloud like Neon)
- Google Gemini API Key

### Step-by-Step Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/umandathathsarani/exoplanet-explorer.git
   ```

2. **Backend Setup**:
   Open a terminal and navigate to the backend app:
   ```sh
   cd exoplanet-explorer/backend
   ```
   *Recommended: Create and activate a Python virtual environment:*
   ```sh
   python -m venv venv
   # Windows: .\venv\Scripts\activate
   # Mac/Linux: source venv/bin/activate
   ```
   Install the required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   Create a `.env` file inside the `backend` directory and add your credentials:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   GEMINI_API_KEYS=your_api_key_here
   ```
   Start the FastAPI server:
   ```sh
   python -m uvicorn app.main:app --reload
   ```
   *The backend API will run on `http://localhost:8000`.*

3. **Frontend Setup**:
   Open a **second** terminal window and navigate to the frontend directory:
   ```sh
   cd exoplanet-explorer/frontend
   ```
   Install NPM dependencies:
   ```sh
   npm install
   ```
   Start the Vite development server:
   ```sh
   npm run dev
   ```
   *The Vue application will run on `http://localhost:5173`.*

4. **Blast Off!** 
   Open your browser and navigate to `http://localhost:5173` to explore the universe!

---

## 📡 Core API Endpoints

The FastAPI backend automatically generates interactive Swagger documentation. When the backend is running, visit `http://localhost:8000/docs` to test endpoints directly.

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/auth/register` | Register a new user | No |
| `POST` | `/api/auth/login` | Authenticate and receive JWT | No |
| `POST` | `/api/exoplanets/search` | Search PostgreSQL for planets | Yes |
| `GET` | `/api/dashboard` | Fetch user's observatory & notes | Yes |
| `PATCH` | `/api/exoplanets/{id}/favorite` | Toggle planet in observatory | Yes |
| `POST` | `/api/exoplanets/{id}/analyze` | Trigger Gemini AI astrophysics report| Yes |

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting Pull Requests to us.

---

## 🛡️ Security

If you discover any security related issues, please refer to our [SECURITY.md](SECURITY.md) for reporting protocols.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

<p align="center">
  <i>Developed with 🌌 by Mummullage Binuri Umanda Thathsarani</i>
</p>