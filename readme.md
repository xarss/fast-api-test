# FastAPI Test Project

This is a test project to learn FastAPI

## Setup

Clone the repository.

```bash
git clone https://github.com/xarss/fast-api-test.git fast-api-test
cd fast-api-test
```

Install requirements.

```bash
pip install -r requirements.txt
```

To run the project. You can also [setup a launch file](#optional-visual-studio-code-configs).
```bash
uvicorn app.main:app --reload
```

## Optional Visual Studio Code configs

`.vscode\launch.json` - Press `F5` anywhere in the project to run the debug.
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

`.vscode\settings.json` - VS Code will not show the `__pycache__` folders.
```json
{
  "files.exclude": {
    "**/__pycache__": true
  }
}
```