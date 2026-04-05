# PWP SPRING 2026
# Music Web API - Beatify

## Group Information

- Student 1. Jalal Ghaffar, jghaffar24@student.oulu.fi
- Student 2. Hidayat Ur Rehman, Hidayat.Rehman@student.oulu.fi
- Student 3. Heikki Tolonen, heikki.tolonen@student.oulu.fi
- Student 4. Teemu Kettukangas, teemu.kettukangas@student.oulu.fi

## Quick Start

Run all commands from project root.

### 1) Install dependencies

```bash
pip install -r Database_folder/requirements.txt
pip install flask-restful pytest pytest-cov
```

### 2) Setup database and start API

```bash
python setup.py
```

This script installs missing dependencies, recreates tables, populates sample data, and starts the API.

### 3) Start API manually (optional)

```bash
python -m Beatify.api
```

API base URL:

```text
http://localhost:5000/Beatify/api/v1
```

## Tests

Run only API test file:

```bash
python -m pytest tests/api_test.py -v
```

Run all tests:

```bash
python -m pytest -v
```

Run coverage:

```bash
python -m pytest tests/api_test.py -v --cov=Beatify --cov-report=term-missing
```

## Documentation Index

- Main app package docs: [Beatify/README.md](Beatify/README.md)
- Database notes and setup details: [Database_folder/README.md](Database_folder/README.md)
- Test guide: [tests/README.md](tests/README.md)
- Schema folder notes: [Beatify/static/schema/README.md](Beatify/static/schema/README.md)

## Docker Deployment (Quick)

Build and run local production-style stack:

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8080/Beatify/api/v1
```

GitHub Actions workflow for CI/CD is in:

```text
.github/workflows/ci-cd.yml
```

Validate OpenAPI locally:

```bash
python -m openapi_spec_validator docs/openapi.yaml
```

## Notes

- The old `app/` package docs are no longer used. Current code lives in the `Beatify/` package.
- If you change folder structure, update imports and scripts (`setup.py`, tests, and DB scripts) accordingly.

