# 🌌 Exoplanet Explorer

> **An integrated full-stack research platform for exploring, tracking, and analyzing exoplanetary data.**

Exoplanet Explorer is a modern web application that combines a PostgreSQL-backed planetary database with Generative AI to help users explore exoplanets and generate scientific insights. The platform provides an intuitive interface for searching planetary data, managing research notes, and producing AI-assisted astrophysical analyses.

---

## 🚀 Features

### 🔍 Search & Filter

Quickly search and filter exoplanets using various scientific parameters, including:

* Discovery Method
* Distance from Earth
* Planetary Mass

### 📝 Research Logs

Manage your research efficiently with complete CRUD functionality.

* Create research notes
* View saved notes
* Update existing notes
* Delete unwanted entries

### ⭐ Favorites

Bookmark and organize your favorite exoplanets for quick access during your research session.

### 🤖 AI-Powered Analysis

Generate professional, academic-style astrophysical reports using the Google Gemini API. The AI can summarize planetary characteristics and provide detailed scientific insights based on available data.

---

## 🛠 Technology Stack

### Frontend

* Vue.js 3
* Vue Script Setup
* Tailwind CSS

### Backend

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL (Neon Database)

### Artificial Intelligence

* Google Gemini API
* Model: `gemini-2.0-flash`

---

## 📦 Getting Started

Follow the steps below to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/exoplanet-explorer.git

cd exoplanet-explorer
```

---

### 2. Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the backend directory and configure the following environment variables.

```env
DATABASE_URL=your_postgresql_connection_string

GEMINI_API_KEYS=your_google_gemini_api_key
```

Start the FastAPI development server.

```bash
uvicorn app.main:app --reload
```

---

### 3. Frontend Setup

Open a new terminal and navigate to the frontend directory.

```bash
cd frontend
```

Install project dependencies.

```bash
npm install
```

Run the development server.

```bash
npm run dev
```

---

## 📁 Project Structure

```text
exoplanet-explorer/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## 🎯 Project Goals

The primary objectives of Exoplanet Explorer are to:

* Simplify exploration of exoplanet datasets.
* Provide an intuitive research workflow.
* Integrate AI-assisted scientific analysis.
* Demonstrate a modern full-stack application architecture using FastAPI and Vue.js.

---

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project, please fork the repository, create a feature branch, and submit a Pull Request. For detailed guidelines, see the **CONTRIBUTING.md** file.

---

## 📄 License

This project is distributed under the **MIT License**. See the **LICENSE** file for more information.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub. Your support helps improve and maintain the project.

---

## 👨‍💻 Author

**Mummullage Binuri Umanda Thathsarani**

Bachelor of Science (Honours) in Information Technology
Specialization in Artificial Intelligence

GitHub: https://github.com/your-username

Passionate about Artificial Intelligence, Machine Learning, Full-Stack Development, and building intelligent software solutions.

