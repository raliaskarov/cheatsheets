# Common commands to use SSH

## folder for ssh
```
mkdir ~/.ssh
hmod 700 ~/.ssh         #700 on the folder means only you can enter it.
chmod 600 ~/.ssh/*      #600 on the files means only you can read/write them.
```


## Creating SSH
ssh key generation
```
ssh-keygen -t rsa -b 4096 -C "<your email address>"
```

or with specified file name
```
ssh-keygen -t ed25519 -f ~/.ssh/<file name> -C "email"
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

**set hosts**

```
nano ~/.ssh/config
```

```
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_github
    IdentitiesOnly yes
```

**view fingerptint of existing key**
```
ssh-keygen -lf ~/.ssh/id_rsa.pub
```

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

## Verify
Example:
```
ssh-keygen -Y verify \
  -f allowed_signers \
  -I contact@grapheneos.org \
  -n "factory images" \
  -s tegu-install-2025120400.zip.sig < tegu-install-2025120400.zip

```
What each part means

-f allowed_signers → file containing GrapheneOS’s public signing key

-I contact@grapheneos.org

→ identity string that must match the one embedded in the signature

-n "factory images" → namespace (must be exactly this string)

-s tegu-install-2025112100.zip.sig → the signature file

< tegu-install-2025112100.zip → the actual factory image

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

