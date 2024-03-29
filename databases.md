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
