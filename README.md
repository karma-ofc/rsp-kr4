# RSP KR4 Project

A FastAPI-based web application for user management with custom exception handling and validation.

## Features

- User creation, retrieval, and deletion
- Custom exception handling (CustomExceptionA and CustomExceptionB)
- Request validation with detailed error messages
- SQLite database with Alembic migrations

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/karma-ofc/rsp-kr4.git
   cd rsp-kr4
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables (copy .env.example to .env and fill in values)

4. Run database migrations:
   ```
   alembic upgrade head
   ```

5. Run the application:
   ```
   uvicorn main:app --reload
   ```

## API Endpoints

- `GET /trigger-a?value=<int>` - Trigger custom exception A
- `GET /trigger-b/{item_id}` - Trigger custom exception B
- `POST /users` - Create a new user
- `GET /users/{user_id}` - Get user by ID
- `DELETE /users/{user_id}` - Delete user by ID

## Testing

Run tests with:
```
pytest
```

## License

This project is licensed under the MIT License.