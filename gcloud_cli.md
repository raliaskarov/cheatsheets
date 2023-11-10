# Guide to deploy app with Google App Engine

## Configuring Google Cloud CLI
Show accounts
```
gcloud auth list
gcloud auth login
gcloud config set account `ACCOUNT`
```

## In Google Cloud CLI install and update packages
```
python -m pip install --upgrade pip
gcloud components install app-engine-python
pip install --upgrade google-api-core
pip install --upgrade google-auth

```

## In widows PowerShell set execution policy
```
Set-ExecutionPolicy RemoteSigned
```


## Deploying app
Create app
```
gcloud app create
```

