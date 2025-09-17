# 🚨 Smart Incident Detection Dashboard  

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success?logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-UI-38B2AC?logo=tailwind-css)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-orange?logo=scikit-learn)

A full-stack project for **network intrusion detection** using **Machine Learning**.  
It demonstrates skills in **data science, backend APIs, frontend development, and system integration**.  

---

## 📸 Demo

![Dashboard Screenshot](docs/demo.png)  
*(Add a screenshot or GIF of your running app here — recruiters love visuals!)*

---

## 📂 Project Structure

smart-incident-dashboard/
│
├── backend/ # FastAPI backend (API + ML model loading)
│ └── app.py
│
├── notebooks/ # Jupyter notebooks & training assets
│ └── models/
│ ├── rf_pipeline.joblib # Trained Random Forest model
│ └── feature_names.json # Features used in training
│
├── frontend/ # React dashboard
│ ├── src/
│ │ ├── App.jsx # Main React app
│ │ ├── main.jsx # Entry point
│ │ └── style.css # Tailwind setup
│ └── ...
│
└── README.md


---

## 🚀 Features

* 🔎 Train & save ML model (Random Forest).  
* ⚡ Serve predictions via FastAPI backend.  
* 🧩 Swagger UI for interactive API testing.  
* 🎨 React + Tailwind dashboard for inputs & predictions.  
* 📊 Recharts pie chart for probability visualization.  
* 🌐 End-to-end workflow: **ML → API → Dashboard**.  

---

## ⚙️ Setup Instructions  

### 1. Backend (FastAPI + ML)  

```bash
# Create venv
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn backend.app:app --reload --port 8000

```
👉 Backend: http://127.0.0.1:8000

👉 Swagger: http://127.0.0.1:8000/docs

2. Frontend (React + Tailwind + Vite)
```bash
cd frontend
npm install
npm run dev
```
👉 Frontend: http://localhost:5173

🖥️ Usage Flow

Start backend (uvicorn) and frontend (npm run dev).

Enter flow features in dashboard form.

Click Predict.

Get results:

✅ Benign (green)

🚨 Attack (red)

📊 Pie chart shows probability breakdown

🔍 Feature Definitions

Flow Duration → Time span of the flow (ms). Long/short flows may indicate benign vs. attack.

Tot Fwd Pkts → Packets sent from source → destination. High values may suggest scans/floods.

Tot Bwd Pkts → Packets sent from destination → source. Imbalance may indicate suspicious traffic.

TotLen Fwd Pkts → Total size (bytes) of forward packets. Helps detect bulk data transfer/exfiltration.

⚡ These are sample features — IDS datasets often use 80+ features.

📊 Example API Request
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "data": {
    "Flow Duration": 1000,
    "Tot Fwd Pkts": 20,
    "Tot Bwd Pkts": 10,
    "TotLen Fwd Pkts": 500
  }
}'
```
Response
```bash
{
  "prediction": 1,
  "probability": [0.0, 1.0]
}

```
0 = Benign

1 = Attack

📖 Learning Outcomes

This project shows experience in:

ML Engineering → Preprocessing, model training, persistence (joblib).

Backend Development → FastAPI, REST APIs, CORS, Swagger docs.

Frontend Development → React hooks, Axios, TailwindCSS, Recharts.

System Integration → Debugging APIs, handling JSON, full-stack design.

📊 Dataset

This project was built using the CICIDS2018 Intrusion Detection Dataset.
Due to GitHub’s file size limits, raw CSV files are not included here.

👉 You can download the dataset from:
CICIDS2018 Dataset – Canadian Institute for Cybersecurity(https://www.unb.ca/cic/datasets/ids-2018.html?)

(In this repo, only a sampled/cleaned version of the dataset was used for model training.)

📌 Credits

Built with ❤️ using:

Python, FastAPI, scikit-learn, joblib (backend & ML)

React, Vite, TailwindCSS, Recharts, Axios (frontend)
