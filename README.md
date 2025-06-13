

```markdown
# 🧮 Loan Calculator App

A simple web application for calculating loan repayment details. It features a **FastAPI** backend and a **Streamlit** frontend. The entire application is containerized using **Docker** and can be deployed easily.

---

## 📦 Tech Stack

- **FastAPI** – Backend API for loan calculations
- **Streamlit** – Frontend UI for user interaction
- **Docker** – Containerization
- **Render** – Deployment platform (optional)

---

## 🚀 Features

- Calculate monthly loan payments
- Responsive web UI using Streamlit
- Clean and simple REST API using FastAPI
- Dockerized for easy deployment

---

## 📁 Project Structure

```

loan-calculator/
├── backend/
│   └── main.py               # FastAPI app for loan calculation
├── frontend/
│   └── app.py                # Streamlit app (frontend)
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
└── README.md                 # Project documentation

````

---

## ⚙️ How to Run Locally (with Docker)

Make sure you have Docker installed, then:

```bash
# Build the Docker image
docker build -t loan-calculator .

# Run the container
docker run -p 8501:8501 loan-calculator
````

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🌍 Live Demo

🔗 [https://your-live-link-on-render.com](https://your-live-link-on-render.com)
*(Replace with your actual Render or deployment URL)*

---

## 📤 API Endpoint (FastAPI)

**POST** `/calculate-loan`

**Request JSON:**

```json
{
  "principal": 50000,
  "annual_rate": 5.0,
  "years": 2
}
```

**Response JSON:**

```json
{
  "monthly_payment": 2193.98
}
```

---

## 🛠️ Built By

 [Haula Namata Muanaisha](mailto:haulanamata99@gmail.com) – Developer & Project Manager

-
