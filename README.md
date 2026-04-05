# PWP SPRING 2026
# Music Web API, Beatify
# Group information
* Student 1. Jalal Ghaffar, jghaffar24@student.oulu.fi
* Student 2. Hidayat Ur Rehman, Hidayat.Rehman@student.oulu.fi
* Student 3. Heikki Tolonen, heikki.tolonen@student.oulu.fi
* Student 4. Teemu Kettukangas, teemu.kettukangas@student.oulu.fi


# Run Beatify API (Current Structure)

Run all commands from the project root folder.

## 1) Install dependencies

```bash
pip install -r Database_folder/requirements.txt
pip install flask-restful pytest pytest-cov
```

## 2) Create and populate database

```bash
python setup.py
```

This script installs requirements (if missing), creates tables, populates sample data, and starts the API.

If you want to run manually without setup script:

```bash
python Database_folder/populate_DB.py
```

## 3) Start API manually

```bash
python -m Beatify.api
```

API base URL:

```text
http://localhost:5000/Beatify/api/v1
```


# Run Tests (Current Structure)

Run from project root:

```bash
python -m pytest tests/api_test.py -v
```

Run all tests:

```bash
python -m pytest -v
```

Run with coverage:

```bash
python -m pytest tests/api_test.py -v --cov=Beatify --cov-report=term-missing
```


# How to setup the API Beatify with the setup.py file

Setting up the API with the setup.py file is super easy and straight forwarded. The file automatically installs required dependencies, creates the database, populates it and starts the flask application.  All you need to do, to access and run this setup.py file, is to:
- navigate to the correct folder where setup.py is located,
- then run python setup.py, this is easily done from CMD

# Problems:
- You should have the file architecture exactly the same as in our github, because otherwise there could be errors in running the setup.py file.
- This is due to how the file is build and organized. You could change the file structure, but in doing so, you would need to do slight changes to setup.py file.
- These apply to test_db.py file as well. So the easiest way is to keep the application file structure the same as ours.  

