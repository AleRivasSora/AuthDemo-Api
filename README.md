# 🚀 FastAPI User Authentication API

A secure and modern API for user registration and authentication built with FastAPI. Features password hashing, CORS support, and robust input validation.

## ✨ Features

- **User Registration** with password hashing (bcrypt)
- **User Login** with credentials verification
- **CORS Middleware** for cross-origin requests
- **Advanced Validation** for:
  - Email format and length
  - Password complexity
  - Name length constraints
- **Secure Data Handling** with Pydantic models

## 🛠️ Technologies Used

- FastAPI
- Pydantic (Data validation)
- Passlib (Password hashing)
- Python 3.7+

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/AleRivasSora/AuthDemo-Api.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚦 Running the Server

Start the development server:

```bash
uvicorn main:app --reload
```

**The API will be available at http://localhost:8000**

## 📚 API Documentation

Interactive documentation available at:

http://localhost:8000/docs

http://localhost:8000/redoc

## 🌐 API Endpoints

- **POST /register:**

  - Creates a new user.
  - Requires `name`, `email`, and `password` in the request body.
  - Returns a 200 OK response with user information on success.
  - Returns a 400 Bad Request if the email already exists.
  - Returns a 422 Unprocessable Entity if the data is not sent correctly.

- **POST /login:**
  - Authenticates the user.
  - Requires `email` and `password` in the request body.
  - Returns a 200 OK response on successful login.
  - Returns a 401 Unauthorized response on failed login.
  - Returns a 422 Unprocessable Entity if the data is not sent correctly.

**Note:**

- This is a simplified example and should not be used for production systems.
- For production, you should:
  - Use a real database (e.g., PostgreSQL, MySQL) to store user data.
  - Implement more robust security measures (e.g., JWT authentication, password reset).
  - Consider using a dedicated user management service.

**Made with ❤️ by Alexander Rivas dev**

**License:** MIT
