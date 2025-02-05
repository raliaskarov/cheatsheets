# Guide to deploye streamlit to Google App Engine

## Files

structure
```
-app.py
-requirements.txt
-Docerfile
-app.yaml

```
app.py
```
import streamlit as st

st.title("App Engine sample app")

name = st.text_input("Your name?")

st.write(f"Hello, {name or 'world'}!")
```

requirements.txt
```
streamlit
```

Dockerfile
```
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt and app.py into the container
COPY requirements.txt ./
COPY app.py ./
COPY streamlit-app.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "$PORT"]

```

app.yaml
```
runtime: python
env: flex

entrypoint: streamlit run streamlit-app.py --server.port $PORT

runtime_config:
    operating_system: "ubuntu22"

network:
  name: projects/emea-controlling-prd/global/networks/default
  subnetwork_name: default-subnet
```


