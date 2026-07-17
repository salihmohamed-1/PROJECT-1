# CogniStream Setup Guide

## Prerequisites

Install the following software before running the project:

- Git
- Python 3.11 or later
- Node.js (LTS)
- VS Code

---

## Clone Repository

```bash
git clone https://github.com/salihmohamed-1/PROJECT-1.git
```

---

## Install Python Packages

```bash
pip install -r requirements.txt
```

---

## Install Frontend Packages

```bash
cd cognistream/frontend
npm install
```

---

## Run Frontend

```bash
npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

## Run Backend (Week 2)

```bash
uvicorn api.main:app --reload
```

Backend URL:

```
http://localhost:8000
```

---

## Project Structure

```
cognistream/
├── ingestion/
├── processing/
├── api/
├── frontend/
├── docs/
├── tests/
```

---

## Troubleshooting

### npm not recognized

Install Node.js and restart VS Code.

### git not recognized

Install Git and restart VS Code.

### Python module errors

Run:

```bash
pip install -r requirements.txt
```

---

Setup Complete ✅