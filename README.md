# 🛒 Product Manager — Full-Stack App

A full-stack product management application built with **FastAPI** (backend) and **React** (frontend). Supports creating, updating, and deleting products through a clean REST API connected to a PostgreSQL database.

---

## 🧱 Tech Stack

| Layer     | Technology                          |
|-----------|-------------------------------------|
| Backend   | FastAPI, SQLAlchemy, psycopg2       |
| Database  | PostgreSQL                          |
| Frontend  | React 18, Axios                     |
| Server    | Uvicorn                             |
| Config    | python-dotenv                       |

---

## 📁 Project Structure

```
project-root/
├── backend/        # FastAPI app
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── .env
│   └── pyproject.toml
└── frontend/       # React app
    ├── src/
    ├── public/
    └── package.json
```

---

## ⚙️ Backend Setup

### Prerequisites
- Python 3.13+
- PostgreSQL running locally

### Installation

```bash
cd backend
pip install .
```

### Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
```

### Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Endpoints

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/products`        | Get all products    |
| GET    | `/products/{id}`   | Get product by ID   |
| POST   | `/products`        | Create a product    |
| PUT    | `/products/{id}`   | Update a product    |
| DELETE | `/products/{id}`   | Delete a product    |

Interactive API docs available at: `http://localhost:8000/docs`

---

## 🖥️ Frontend Setup

### Prerequisites
- Node.js & npm

### Installation

```bash
cd frontend
npm install
```

### Run the App

```bash
npm start
```

The app will be available at `http://localhost:3000` and proxies API requests to `http://localhost:8000`.

---

## 🚀 Running the Full Stack

1. Start PostgreSQL
2. Start the backend:
   ```bash
   cd backend && uvicorn main:app --reload
   ```
3. Start the frontend:
   ```bash
   cd frontend && npm start
   ```

---

## 📄 License

MIT
