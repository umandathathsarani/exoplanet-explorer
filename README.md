<div align="center">
  <img src="https://images.openai.com/static-rsc-4/Bcv5Q6UQQUhxi7-_X2voNIOZFAXiU0XrS7Sg-Y5xg6keiKzgYZz2MUObtIhL67e9Mh_qrbEi6Kp_0uCC72piiiBDD-aHvazFIghf-hUdYY2GKmS-9EqXGQxIJN1UvsgT491Jtw-ORa_HHEPo-bbhRAdEUGVRKuabxD6k5uJepLI1l9G6YOAC6ZD6qR5ouJaw?purpose=fullsize" alt="Exoplanet Explorer Logo" width="100%">
  
  <br />
  <h1>🌌 Exoplanet Explorer</h1>
  <p><strong>A breathtaking, interactive web application dedicated to the discovery, classification, and science of planets beyond our Solar System.</strong></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
  [![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs)](https://vuejs.org/)
  [![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
  [![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat)](CONTRIBUTING.md)

</div>

<br />

<details open>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li><a href="#-about-the-project">About The Project</a></li>
    <li><a href="#-screenshots">Screenshots</a></li>
    <li><a href="#-key-features">Key Features</a></li>
    <li><a href="#-project-architecture">Project Architecture</a></li>
    <li><a href="#-getting-started">Getting Started (Local Setup)</a></li>
    <li><a href="#-tech-stack">Tech Stack</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-contact--creator">Contact & Creator</a></li>
  </ol>
</details>

---

## 📖 About The Project

**Exoplanet Explorer** is an educational platform designed to bring the wonders of astrobiology and astrophysics to the general public. Built with modern web technologies, it features a deeply immersive, dark-themed space interface that scales beautifully from massive desktop observatories down to mobile screens.

The application serves as both a reference tool and an interactive learning environment, bridging the gap between raw scientific data and accessible public education.

Currently, Exoplanet Explorer is a **frontend-only Single Page Application (SPA)**. There is no dedicated backend server yet; all state and authentication are simulated locally in the browser to ensure a lightning-fast experience. Live API integrations are planned for Phase 2!

---

## 📸 Screenshots

<div align="center">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182754.png" alt="Exoplanet Explorer View 1" width="48%">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182810.png" alt="Exoplanet Explorer View 2" width="48%">
</div>
<div align="center">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182834.png" alt="Exoplanet Explorer View 3" width="48%">
  <img src="frontend/public/screenshots/Screenshot%202026-06-28%20182849.png" alt="Exoplanet Explorer View 4" width="48%">
</div>

---

## ✨ Key Features

- 📚 **Comprehensive 10-Chapter Textbook**
  - Dive deep into astronomy with beautifully formatted, responsive modules covering everything from planetary classification to the search for extraterrestrial biosignatures.
- 🧠 **Interactive Quiz System**
  - Test your knowledge with a multi-level testing system (Easy, Medium, Hard, and Bonus Challenges). Features dynamic real-time scoring, locking answers, and detailed post-submission explanations.
- 🎨 **Immersive Cinematic UI**
  - A stunning, space-themed dark mode interface powered by TailwindCSS. Features micro-animations, glowing interactive elements, and glassmorphism components.
- 🔐 **User Authentication & Dashboard**
  - A built-in user system allowing users to log in (including simulated Microsoft OAuth) and access a personalized "My Observatory" dashboard.
- 📱 **Fully Responsive**
  - Meticulously designed grid layouts ensure the interface looks perfect on mobile devices, tablets, and large desktop screens.

---

## 🏗️ Project Architecture

Exoplanet Explorer is a full-stack application built with a Vue 3 frontend and a Python FastAPI backend. The repository is structured to cleanly separate the client and server concerns.

```text
exoplanet-explorer/
├── backend/                    # Python FastAPI Server
│   ├── main.py                 # Core API endpoints & logic
│   └── requirements.txt        # Python dependencies
├── frontend/                   # Vue 3 SPA Client
│   ├── public/                 # Static assets (favicons, screenshots)
│   └── src/
│       ├── assets/             # Logos and SVGs
│       ├── components/         # Reusable Vue Components
│       │   ├── lessons/        # The 10-Chapter Interactive Textbook modules
│       │   │   ├── Chapter1.vue  -> Chapter10.vue
│       │   ├── AuthModal.vue   # Login/Signup interface
│       │   ├── Dashboard.vue   # User Observatory Profile
│       │   ├── ExoplanetChart.vue
│       │   ├── ExoplanetSearch.vue
│       │   ├── LandingPage.vue # Cinematic home page
│       │   ├── Lessons.vue     # Core router for the textbook
│       │   └── Quizzes.vue     # Multi-level scoring system
│       ├── App.vue             # Main application layout and navigation
│       ├── main.js             # Vue application entry point
│       ├── state.js            # Global state management (Auth, etc.)
│       └── style.css           # Global Tailwind directives & custom CSS
├── .github/                    # Issue and PR templates
├── CHANGELOG.md                # Version history
├── ROADMAP.md                  # Future project goals
└── README.md
```

---

## 🚀 Getting Started (Local Setup)

Because this project is currently a frontend-only application (without a heavy backend database), setting it up locally is incredibly fast and easy. Follow these exact steps to run Exoplanet Explorer on your machine.

### Prerequisites

You need [Node.js](https://nodejs.org/) (which comes with `npm`) installed on your machine.
To check if you have it installed, open your terminal and run:
```sh
node -v
npm -v
```

### Step-by-Step Installation

1. **Clone the repository** to your local machine:
   ```sh
   git clone https://github.com/umandathathsarani/exoplanet-explorer.git
   ```

2. **Configure the Database**:
   Create a `.env` file in the `backend` directory and add your PostgreSQL connection string:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   GEMINI_API_KEYS=your_api_key_here
   ```

3. **Start the Backend (Python / FastAPI)**:
   Open a terminal and navigate to the `backend` directory:
   ```sh
   cd exoplanet-explorer/backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
   *The backend will now be running on `http://localhost:8000`.*

3. **Start the Frontend (Vue 3 / Vite)**:
   Open a *second* terminal and navigate into the `frontend` directory:
   ```sh
   cd exoplanet-explorer/frontend
   npm install
   npm run dev
   ```
   *The frontend will now be running on `http://localhost:5173`.*

4. **Open your browser** and navigate to `http://localhost:5173`.

🎉 **That's it!** You are now running the full-stack application (Frontend + Backend) locally.

---

## 💻 Tech Stack

### Frontend
- **Framework**: Vue 3 (Composition API)
- **Styling**: TailwindCSS
- **Build Tool**: Vite
- **Icons**: Heroicons & Custom SVGs

### Backend
- **Framework**: Python FastAPI
- **Database**: PostgreSQL (via SQLAlchemy)
- **AI Integration**: Google Gemini 2.0 Flash
- **Authentication**: JWT (JSON Web Tokens)

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". 

Please read our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md) for more details.

---

## 📜 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

---

## 👨‍🚀 Contact & Creator

**Mummullage Binuri Umanda Thathsarani**  
_Bachelor of Science Honours in Information Technology (Specialized in Artificial Intelligence)_

* 📧 Email: umathathsarani2003@gmail.com
* 📱 WhatsApp: 0742813833
* 💼 [LinkedIn](https://www.linkedin.com/in/binuri-umanda-859bba337)
* 📸 [Instagram](https://www.instagram.com/b.uma.t)
* 🐙 [GitHub](https://github.com/umandathathsarani)

<br />
<p align="center">
  <i>"Is life rare, or is it everywhere waiting to be found?"</i>
</p>