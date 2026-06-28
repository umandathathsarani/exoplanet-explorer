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
    <li><a href="#-key-features">Key Features</a></li>
    <li><a href="#-project-architecture">Project Architecture</a></li>
    <li><a href="#-getting-started">Getting Started</a></li>
    <li><a href="#-tech-stack">Tech Stack</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-contact--creator">Contact & Creator</a></li>
  </ol>
</details>

---

## 📖 About The Project

**Exoplanet Explorer** is an educational platform designed to bring the wonders of astrobiology and astrophysics to the general public. Built with modern web technologies, it features a deeply immersive, dark-themed space interface that scales beautifully from massive desktop observatories down to mobile screens.

The application serves as both a reference tool and an interactive learning environment, bridging the gap between raw scientific data and accessible public education.

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

Exoplanet Explorer is built as a Single Page Application (SPA) using Vue 3. The repository is structured to separate concerns, keeping routing, state management, and UI components modular.

```text
exoplanet-explorer/
├── frontend/
│   ├── public/                 # Static assets (favicons, background images)
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

## 🚀 Getting Started

Follow these steps to get a local development environment up and running.

### Prerequisites

You need [Node.js](https://nodejs.org/) and npm installed on your machine.
```sh
npm install npm@latest -g
```

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/umandathathsarani/exoplanet-explorer.git
   ```
2. **Navigate to the application directory**
   ```sh
   cd exoplanet-explorer/frontend
   ```
3. **Install NPM dependencies**
   ```sh
   npm install
   ```
4. **Start the Vite development server**
   ```sh
   npm run dev
   ```
5. Open your browser and navigate to `http://localhost:5173`.

---

## 💻 Tech Stack

* **[Vue 3](https://vuejs.org/)**: The progressive JavaScript framework (using Composition API).
* **[Vite](https://vitejs.dev/)**: Next-generation frontend tooling for blazing fast builds.
* **[Tailwind CSS](https://tailwindcss.com/)**: A utility-first CSS framework for rapid UI development.

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
