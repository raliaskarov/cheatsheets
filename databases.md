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
