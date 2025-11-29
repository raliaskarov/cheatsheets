# Guide to install development server on linux

## Create a non-root user (recommended)

SSH into server:

```
ssh root@YOUR_SERVER_IP
```

Create a user named dev:
```
adduser dev
usermod -aG sudo dev
```

Copy your SSH key to that user:
```
rsync -av ~/.ssh/id_ed25519.pub dev@YOUR_SERVER_IP:/home/dev/.ssh/authorized_keys
```

Log in as dev:
```
ssh dev@YOUR_SERVER_IP
```


## Install code-server

Run the official install script:
```
curl -fsSL https://code-server.dev/install.sh | sh
```

Enable the service:
```
sudo systemctl enable --now code-server@$USER
```

## Configure code-server (port, password)

Edit the config:
```
nano ~/.config/code-server/config.yaml
```

Change:
```
bind-addr: 0.0.0.0:8080
auth: password
password: YOUR_STRONG_PASSWORD
cert: false
```

Restart:
```
systemctl --user restart code-server
```

Open firewall if needed
```
sudo ufw allow 8080
``1

Access from any browser
```
http://YOUR_SERVER_IP:8080
```

## Make HTTPS
Install Caddy (automatic SSL certificates):
```
sudo apt install -y caddy
```

Create a domain (optional) and point DNS A record to your server’s IPv4.

Edit:
```
sudo nano /etc/caddy/Caddyfile
```

Add:
if domain:
```
dev.mydomain.com {
    reverse_proxy 127.0.0.1:8080
}
```

if no domain:
```
http://YOUR_SERVER_IP {
    reverse_proxy 127.0.0.1:8080
}
```

Reload:
```
sudo systemctl reload caddy
```

Now you access:

https://dev.mydomain.com
