# Todo API

This is a Django REST framework-based API for managing todo items. The API uses token-based authentication and ensures that users can only access their own todos.

## Features
- Token-based authentication
- CRUD operations for todo items
- User-specific data access

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- Obtain token: `POST /api-token-auth/`
  - Request body: `{ "username": "your_username", "password": "your_password" }`
  - Response: `{ "token": "your_auth_token" }`

### Todos
- List all todos: `GET /todos/`
- Retrieve a specific todo: `GET /todos/{id}/`
- Create a todo: `POST /todos/`
- Update a todo: `PUT /todos/{id}/`
- Delete a todo: `DELETE /todos/{id}/`

### Permissions
- Only authenticated users can access the API.
- Users can only view and manage their own todos.

## Running Tests
Run the following command to execute the tests:
```sh
python manage.py test
```

## License
This project is licensed under the MIT License.

