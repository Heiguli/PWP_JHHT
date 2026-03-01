# Database Setup Guide

You should be using a virtual Python environment to use this database, to not mess up with your own Python environment locally installed on your PC/laptop.

## Setting Up a Virtual Environment

> These instructions are taken from the [Lovelace Exercise 1 page](https://lovelace.oulu.fi/ohjelmoitava-web/ohjelmoitava-web/introduction-to-web-development/).

Starting with version 3.3 of Python, all the necessary tools are automatically included. In case they are not, you need to install [Pip](https://pip.pypa.io/en/stable/installation/) and use it to install the `venv` module. To create a virtual environment, type:

```bash
python3 -m venv /path/to/the/virtualenv
```

On OS X and most Linux distributions you need to use `python3` instead (running the above command on Python 2 will result in an error message that says *"No module named venv"*). The virtualenv will be a normal folder on your file system.

### Activating the Virtual Environment

**Windows:**

```bat
c:\path\to\the\virtualenv\Scripts\activate.bat
```

**OS X / Linux:**

```bash
source /path/to/the/virtualenv/bin/activate
```

After activation you will see the name of your virtualenv in parentheses in front of your command prompt. E.g. if we made an environment called "pwp-env" in the home directory, a command prompt would look like:

```
(pwp-env) user@system:~/pwp-env$
```

## Dependencies

Next are the dependencies needed to run this database from the virtual environment. When you are **inside** your virtual environment, run the `pip install` commands below:

| Package | Version | Install Command |
|---------|---------|-----------------|
| Flask | 3.1.2 | `pip install Flask` |
| Flask-SQLAlchemy | 3.1.1 | `pip install Flask-SQLAlchemy` |
| SQLAlchemy | 2.0.46 | `pip install SQLAlchemy` |
| pysqlite3 | 0.6.0 | `pip install pysqlite3` |

We used **SQLite** database and the version we used was **3.1.1**.

> **Note:** This database might not be the final version, since it will probably get some little tweaks or improvements. But the idea and groundwork behind the database and how it will work is implemented and will be the same in the final version.

## Usage

To use the database locally and try it out:

1. In the folder where your virtual environment is located, create a new folder named to your liking.
2. Add the `database.py` and `populate_dp.py` files to that folder.
3. In your terminal (with the virtual environment activated), navigate to that folder.
4. Create the database:
   ```bash
   python database.py
   ```
   This creates the `test.db` file.
5. Populate the database:
   ```bash
   python populate_dp.py
   ```
   This populates the database with the data defined in `populate_dp.py`. You can change the data to your liking.
