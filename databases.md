# Connect streamlit app to dynamo DB
```
import streamlit as st
import pandas as pd
import boto3
from io import BytesIO

# Set up boto3 client
dynamodb = boto3.resource('dynamodb', region_name='your-region', aws_access_key_id='your-access-key',
                          aws_secret_access_key='your-secret-key')

table = dynamodb.Table('your-table-name')

# Upload data to Streamlit app
uploaded_file = st.file_uploader("Choose an excel file", type=['xlsx'])

if uploaded_file is not None:
    # Read the file into a pandas dataframe
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    # Iterate through each row of the dataframe and upload it to DynamoDB
    for index, row in df.iterrows():
        item = row.to_dict()  # Convert row to dict
        table.put_item(Item=item)  # Put item in DynamoDB

```

# Postgre SQL on Linux Arch

## Install PostgreSQL
Install
```
sudo pacman -Syu postgresql
```


Initialise and start
```
sudo -iu postgres
initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'
exit

sudo systemctl enable postgresql
sudo systemctl start postgresql
```

Create user
```
sudo -iu postgres
psql
```
In shell
```
CREATE USER myuser WITH PASSWORD 'mypassword';
CREATE DATABASE mydb OWNER myuser;
\q
exit
```

## Install PGAdmin
```
mkdir pgadmin
cd pgadmin
pyhon -m venv env
source env/bin/activate
pip install pgadmin4
```

In pgadmin folder create ```config_local.py```:
```
import os

DATA_DIR = os.path.expanduser('~/.pgadmin')
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin.log')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin.db')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')

SERVER_MODE = False
```

In pgadmin folder create data directory
```
mkdir -p ~/.pgadmin
```

## Launch PGAdmin
Visit http://127.0.0.1:5050
Add server:
Log in, then:

    Right-click on Servers → Create → Server

    In the General tab, set Name to Local PostgreSQL

    In the Connection tab, enter:

        Host name / address: localhost

        Port: 5432

        Username: postgres (or your DB user)

        Password: (leave blank or enter your DB password)

        Check Save Password

    Click Save

## Django integration
Create ```settings.py```
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Install PostgreSQL driver for django
```
pip install psycopg2-binary
```

Confirm it works
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



Then visit:

    http://127.0.0.1:8000 to see your Django app

    http://127.0.0.1:5050 to access pgAdmin

## In PGAdmin see tables:
Servers → Local PostgreSQL → Databases → mydb → Schemas → public → Tables


# Django manage.py Command Glossary

This glossary provides an overview of frequently used Django `manage.py` commands and what they do.

## Commands

### `runserver`
**Usage:**  
```bash
python manage.py runserver
```
**Description:**  
Starts a lightweight development web server on the local machine.

---

### `migrate`
**Usage:**  
```bash
python manage.py migrate
```
**Description:**  
Applies database migrations. It creates or updates tables in the database to match Django models.

---

### `makemigrations`
**Usage:**  
```bash
python manage.py makemigrations
```
**Description:**  
Generates new migration files based on changes in models.

---

### `createsuperuser`
**Usage:**  
```bash
python manage.py createsuperuser
```
**Description:**  
Creates a new admin (superuser) account to access the Django admin interface.

---

### `shell`
**Usage:**  
```bash
python manage.py shell
```
**Description:**  
Opens an interactive Python shell preloaded with Django context (models, settings, etc.).

---

### `startapp <app_name>`
**Usage:**  
```bash
python manage.py startapp blog
```
**Description:**  
Creates a new Django application folder structure with default files.

---

### `startproject <project_name>`
**Usage:**  
```bash
django-admin startproject myproject
```
**Description:**  
Creates a new Django project with settings, URLs, and wsgi/asgi config.

---

### `check`
**Usage:**  
```bash
python manage.py check
```
**Description:**  
Checks the entire Django project for common errors without running migrations or starting the server.

---

### `showmigrations`
**Usage:**  
```bash
python manage.py showmigrations
```
**Description:**  
Displays a list of all migrations and their applied/unapplied status.

---

### `sqlmigrate <app_name> <migration_name>`
**Usage:**  
```bash
python manage.py sqlmigrate blog 0001
```
**Description:**  
Displays the SQL statements for a given migration.

---

### `collectstatic`
**Usage:**  
```bash
python manage.py collectstatic
```
**Description:**  
Collects all static files into one directory for deployment.

---

### `flush`
**Usage:**  
```bash
python manage.py flush
```
**Description:**  
Deletes all data from the database and resets it to the initial state.

---

### `loaddata <fixture_file>`
**Usage:**  
```bash
python manage.py loaddata data.json
```
**Description:**  
Loads data from a fixture file into the database.

---

### `dumpdata`
**Usage:**  
```bash
python manage.py dumpdata > data.json
```
**Description:**  
Outputs all data in the database as a JSON fixture.

---

## Notes

- Always activate your virtual environment before using these commands.
- Use `--help` with any command for more options. For example:
  ```bash
  python manage.py migrate --help
  ```
