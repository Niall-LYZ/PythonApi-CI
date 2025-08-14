# PythonApi-CI

A simple FastAPI project with CI/CD integration using GitHub Actions.

## Features
- FastAPI application with health and root endpoints
- Automated testing with pytest
- Code formatting enforced with Black
- Linting with Flake8
- Continuous Integration via GitHub Actions

## Why It Matters
DevSecOps favors shift‑left quality. Pre‑commit enforces formatting/linting before code hits CI, reducing noise and drift between laptops and pipelines.

## Project Structure
```
├── src/
│   └── app.py           # FastAPI application
├── tests/
│   └── test_app.py      # Pytest tests for the API
├── requirements.txt     # Main dependencies
├── requirements-dev.txt # Dev dependencies (pytest, black, flake8)
├── pyproject.toml       # Tool configuration (Black, Flake8)
├── .github/workflows/ci.yml # GitHub Actions workflow
```

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt -r requirements-dev.txt
   ```

## Running Locally
Start the FastAPI app:
```powershell
uvicorn src.app:app --reload
```

## Testing
Run tests with:
```powershell
python -m pytest
```

## Code Quality
- Format code: `black .`
- Lint code: `flake8 .`

## CI/CD
On every push or pull request to `main`, GitHub Actions will:
- Install dependencies
- Check code formatting
- Lint code
- Run tests

See `.github/workflows/ci.yml` for details.
