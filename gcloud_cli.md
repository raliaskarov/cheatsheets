# Guide to deploy app with Google App Engine

## Configuring Google Cloud CLI
Show accounts
```
gcloud auth list
gcloud auth login
gcloud config set account `ACCOUNT`
```

## Manage projects
```
gcloud projects list
gcloud config set project PROJECT_ID

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
## Deploy
```
gcloud app deploy
gcloud app deploy --verbosity=debug
```

## Debug
```
gcloud app logs tail -s default
```

# Cloud Run

## Make container
```
gcloud builds submit --config cloudbuild.yaml
```

## Deploy
Open to internet
```
gcloud run deploy your-service-name --image gcr.io/your-project-id/your-image-name --platform managed --region your-region --allow-unauthenticated
```
Restricted, requires authentication
```
gcloud run deploy your-service-name --image gcr.io/your-project-id/your-image-name --platform managed --region your-region --no-allow-unauthenticated
```
Replace your-service-name, your-project-id, your-image-name, and your-region with your specific details. The --allow-unauthenticated flag makes your app publicly accessible. If your application requires authentication, you might want to omit this flag and configure the appropriate access controls.

# Security
View token
```
gcloud auth print-identity-token
```
Test auth
```
ID_TOKEN=$(gcloud auth print-identity-token)
curl -H "Authorization: Bearer ${ID_TOKEN}" https://emea-controlling-prd-wbp3665ika-ew.a.run.app/
```
