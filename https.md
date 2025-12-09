Guide to enable https.md

Assuming you have mydomainname.com

Check caddy
```
which caddy
systemctl status caddy
```

install if required

enable

```
sudo systemctl enable --now caddy
```

Edit config
```
nano /etc/caddy/Caddyfile
```


```
# here is new section
mydomainname.com {
    respond "Portfolio coming soon!"
}
# here is another section
subdomain.mydomainname.com {
    reverse_proxy 127.0.0.1:8000
}
```

reload
```
sudo systemctl reload caddy
```

