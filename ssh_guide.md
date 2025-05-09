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

**adding to github**
copy pub key
```
cat ~/.ssh/id_rsa.pub | clip
cat ~/.ssh/id_rsa.pub | wl-copy
```
past this key to github > settings > ssh keys > add ssh key

**use**
authenticate - will look for private key in ~/.ssh by default
```
ssh git@github.com
```

use key from custom folder
```
ssh -i /path/to/your/key git@github.com
```

copy key to usb
```
cp ~/.ssh/id_rsa /media/usb/my_id_rsa
cp ~/.ssh/id_rsa.pub /media/usb/my_id_rsa.pub
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

