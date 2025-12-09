guide to set up jupyterhub

From docker image on HTTPS behind reverse proxy on Caddy
```
docker run -d \
  --name jupyterhub \
  -p 127.0.0.1:8000:8000 \
  -v /home/dev/jhub/jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py \
  quay.io/jupyterhub/jupyterhub \
  jupyterhub -f /srv/jupyterhub/jupyterhub_config.py
```
