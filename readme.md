# FastAPI Test Project

This is a test project to learn **FastAPI** and build a REST API with database support, migrations, and Swagger UI.

## Setup

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/xarss/fast-api-test.git fast-api-test
cd fast-api-test
```

### 2. Install dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set up the database

This project uses **SQLAlchemy** for ORM-based database interaction and **Alembic** for migrations. To set up the database, you'll need to configure the **database URL** in a `.env` file.

#### Create a `.env` file

In the project root directory, create a `.env` file and specify your database connection string:

```ini
# .env

DATABASE_URL=mysql://root:yourpassword@localhost:3306/your_database_name
```

### 4. Set up the database and apply migrations

This project uses **Alembic** for managing database migrations. Alembic automatically generates migration scripts based on changes to your models.

To apply the migrations, run the following commands:

1. **Generate the migration script**:
```bash
alembic revision --autogenerate -m "Descriptive short message"
```

2. **Apply the migration** to create the database schema:
```bash
alembic upgrade head
```

### 5. Running the project

To start the FastAPI app with **Uvicorn**, use the following command:

```bash
uvicorn app.main:app --reload
```

The application can be accessed at the following URLs:

* `http://127.0.0.1:8000`: API endpoints
* `http://127.0.0.1:8000/docs`: Swagger UI for API documentation

### 6. Optional Visual Studio Code configs

If you're using **Visual Studio Code**, you can set up debugging and exclude `__pycache__` directories.

#### `.vscode/launch.json`

Press `F5` anywhere in the project to run the debug session.

```json
{
  "configurations": [
    {
      "name": "Run Uvicorn",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--reload"
      ],
      "jinja": true
    }
  ]
}
```

#### `.vscode/settings.json`

This will prevent **VS Code** from showing the `__pycache__` folders.

```json
{
  "files.exclude": {
    "**/__pycache__": true
  }
}
```

## Database Migrations with Alembic

### 1. **Setting up Alembic for database migrations**

Alembic is used to handle **database migrations** and is integrated with **SQLAlchemy**. This allows you to make schema changes to the database without losing existing data.

#### How Alembic Works:

* **`alembic.ini`**: Contains Alembic settings.
* **`env.py`**: Configures Alembic to use the models and their metadata when generating migration scripts.
* **Migrations**: You create migrations by running `alembic revision --autogenerate`. Alembic compares the current database schema with your SQLAlchemy models and generates a migration file.

### 2. **How to Use Alembic for Migrations**

* **Generate a migration script**:
  Whenever you make changes to the models (like adding a new column), you can generate a migration script using:

  ```bash
  alembic revision --autogenerate -m "Description of changes"
  ```

* **Apply the migration**:
  Apply the migration by running:

  ```bash
  alembic upgrade head
  ```

  This will apply all pending migrations and update the database schema.

* **Revert a migration**:
  To rollback to a previous migration:

  ```bash
  alembic downgrade -1  # Reverts the last migration
  ```

### 3. **Viewing Migrations in Swagger UI**

* The **Swagger UI** at `http://127.0.0.1:8000/docs` automatically reflects the changes you make to your API models. Any changes to the endpoints or new routes will appear here.
* You can test endpoints directly from the Swagger UI.

### 7. Additional Notes

* **SQLAlchemy Models**: The models are defined in the `app/models/` folder. They are used to interact with the database using SQLAlchemy ORM.
* **Pydantic Models**: Validation and response serialization are handled by **Pydantic** models. These models ensure that the incoming requests and outgoing responses conform to the expected structure.