# 🚗 Car Insurance Simulator API

An API that simulates car insurance calculation based on the provided vehicle and policy information. This project was developed as part of a backend technical challenge.

---

## 📦 Technologies Used

- Python 3.11
- FastAPI
- Pydantic
- Docker
- Pytest

---

## ▶️ How to Run Locally

### 1. Clone the project

```bash
git clone https://github.com/seu-usuario/car-insurance-simulator.git
cd car-insurance-simulator
```

### 2. Create a virtual environment and install dependencies

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2.1 Configuração do Ambiente

    Copie o arquivo `.env.example` e renomeie para `.env`:

### 3. Run the application

```bash
uvicorn main:app --reload
```

Access the interactive documentation::  
📌 http://127.0.0.1:8000/docs

---

## 🧪 Running the Tests

### Run all tests

```bash
pytest
```

### Run unit tests

```bash
pytest tests/unit
```

### Run integration tests

```bash
pytest tests/integration
```

---

## 🐳 How to Run with Docker

### 1. Build the image

```bash
docker build -t car-insurance-simulator .
```

### 2. Run the container

```bash
docker run -d -p 8000:8000 car-insurance-simulator
```

Access the API in your browser:  
📌 http://localhost:8000/docs

---

## 🐙 Run Tests Inside Docker (optional)

### 1. Access the container

```bash
docker run -it car-insurance-simulator /bin/bash
```

### 2. Run the tests

```bash
pytest
```
## 📌 Notes

- Project organized in layers following best practices for separation of concerns.
- Easy to extend with new calculation rules or data sources.
- Clean and testable code focused on readability.

