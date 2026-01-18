How to set up anki server for flash cards


Venv
```
python3 -m venv ~/.vevns/anki-sync-server
source ~/.vevns/anki-sync-server/bin/activate
```

Install
```
pip install anki
```

Start
```
SYNC_USER1=user:pass ~/syncserver/bin/python -m anki.syncserver
```

***
Or make it a service

Make
```
sudo nano /etc/systemd/system/ankisync.service
```

Paste
```
[Unit]
Description=Anki Self-Hosted Sync Server
After=network.target

[Service]
# User who will run the service
User=dev          
# credentials (for anki user)
Environment=SYNC_USER1=user:pass 
# data
Environment=SYNC_BASE=/home/user/anki_data
# set host and port
Environment=SYNC_HOST=0.0.0.0
Environment=SYNC_PORT=8081
ExecStart=/home/user/.venvs/anki-sync-server/bin/python -m anki.syncserver
Restart=always
RestartSec=5

```


Launch

```
sudo systemctl daemon-reload
sudo systemctl enable --now ankisync.service
udo systemctl status ankisync.service
```
