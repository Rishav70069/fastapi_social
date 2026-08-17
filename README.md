# FastAPI Tutorial Project

This is a basic social media-like API project created while learning **FastAPI**. The project implements core concepts including RESTful API design, database integration with an ORM, user authentication, and authorization.

## 🚀 Features

- **User Management**: 
  - User registration and profile management.
  - Secure password hashing using `passlib` and `bcrypt`.
- **Authentication & Authorization**:
  - JWT (JSON Web Token) based authentication.
  - OAuth2 implementation for securing endpoints.
- **Post Management**:
  - Create, Read, Update, and Delete (CRUD) operations for posts.
  - Posts are linked to their owners (Users).
  - Publication status control.
- **Voting System**:
  - Ability for users to vote on posts.
  - Many-to-many relationship between Users and Posts.
- **Database Migrations**:
  - Integrated with `Alembic` for version-controlled database schema changes.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3.x
- **Database**: PostgreSQL (via `psycopg`)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
- **Auth**: `python-jose` (JWT), `passlib` (Password hashing)
- **Server**: `uvicorn`

## 📋 Project Structure

```text
.
├── alembic/               # Database migration scripts
├── app/
│   ├── routers/           # API Route handlers
│   │   ├── auth.py        # Authentication endpoints
│   │   ├── post.py        # Post management endpoints
│   │   ├── user.py        # User management endpoints
│   │   └── vote.py        # Voting endpoints
│   ├── config.py         # Application configuration
│   ├── database.py        # Database connection and session management
│   ├── main.py            # Application entry point
│   ├── models.py          # SQLAlchemy database models
│   ├── oauth2.py         # OAuth2 and JWT utility functions
│   ├── schemas.py         # Pydantic schemas for data validation
│   └── utility.py         # General helper functions
├── alembic.ini            # Alembic configuration
└── requirements.txt       # Project dependencies
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL database

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rishav70069/fastapi_social
   cd fastapi
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**:
   Ensure your PostgreSQL database is running and update the database URL in `app/config.py` (or your environment variables).

5. **Run Migrations**:
   ```bash
   alembic upgrade head
   ```

### Running the Application

Start the server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
