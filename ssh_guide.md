# Common commands to use SSH

## Creating SSH
ssh key generation
```
ssh-keygen -t rsa -b 4096 -C "<your email address>"
```

cs into .ssh
```
cd ~/.ssh
```

start ssh agent
```
eval "$(ssh-agent -s)"
```

add key to ssh agent
```
ssh-add ~/.ssh/id_rsa
```


## Keyboard forwarding on Putty

1. Launch PuTTY on your PC.
2. Enter the IP address of your LibreELEC device in the "Host Name (or IP address)" field.
3. Select the connection type (usually SSH).
4. In the left-hand navigation pane, go to "Connection" -> "SSH" -> "Auth".
5. Check the box next to "Enable X11 forwarding" to enable X11 forwarding.
6. In the left-hand navigation pane, go to "Connection" -> "SSH" -> "X11".
7. Check the box next to "Enable X11 forwarding" to enable X11 forwarding.
8. In the "X display location" field, enter localhost:0.0.
9. Go back to the "Session" category in the left-hand navigation pane.
10. Click on "Save" to save the changes as a new session.
11. Click "Open" to initiate the SSH connection.

