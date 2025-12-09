guide to set up jupyterhub

jupyterhub_config.py:
See current 
```
grep -v '^\s*#' jupyterhub_config.py | grep -v '^\s*$'
```

set to
```
c = get_config()  #noqa
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'
c.Authenticator.allow_all = True
```

From docker image on HTTPS behind reverse proxy on Caddy
```
docker run -d \
  --name jupyterhub \
  -p 127.0.0.1:8000:8000 \
  -v /home/dev/jhub/jupyterhub_config.py:/srv/jupyterhub/jupyterhub_config.py \
  quay.io/jupyterhub/jupyterhub \
  jupyterhub -f /srv/jupyterhub/jupyterhub_config.py
```

Confirm it works
```
curl -v http://127.0.0.1:8000
curl -v https://lab.raliaskarov.com
```

if changing configfile
```
docker stop jupyterhub
docker rm jupyterhub
```
relaunch docker

add users
```
docker exec -it jupyterhub bash
```

in shell
```
useradd -m roman
passwd roman
exit
```

**Troubleshooting**
view logs
```
docker logs jupyterhub --tail=30
```
