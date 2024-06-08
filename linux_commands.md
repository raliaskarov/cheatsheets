# Software management
## yum/get-apt
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|`$ yum list installed `| show intalled|
|`$ sudo yum update`|update all|
|`$ sudo yum update openssl`|update 1 pack|
|`yum repolist all`|show installed repos|
|`$ sudo yum search "find"`|find package|
|`$ sudo yum-config-manager --add-repo https://www.example.com/repository.repo` | add repo|
|`$ sudo yum install <PACKAGE>`|install package|

Install deb package
```
wget https://download.nomachine.com/download/7.10/Raspberry/nomachine_7.10.1_1_armhf.deb
sudo dpkg -i nomachine_7.10.1_1_armhf.deb
sudo apt --fix-broken install
```
## Working with pip
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|`sudo pip3 install -r requirements.txt`|install pacs from requirements
# Files managmenet
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|`$ rmdir <DIRECTORY>`|remove EMPTY directory|
|`$ rm -r <DIRECTORY>`|remove not empty directory with all contents **without prompting**|
|`$ rm -i <FILENAME>` | Remove file with prompring y/n|
|`$ rm \*.pdf`| Remove all .pdf files|
# Navigation
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|` $ pwd`| Print working directory|
# Terminal
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|`tmux new -s <SessionNameGoesHere>`|start new session|
|`[Ctrl+B], <release>, [D]`|detatch session|
|`tmux attach`|attch latest session|
|`tmux attach -t <SessionNameGoesHere>`|attch specific session|
|` $ tmux kill-session`|close tmux session|
# Archives
|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|` $ 7za e <PATH_TO_ARCHIVE>`|Extract files from archive (without using directory names)|
[7za help](https://www.mankier.com/1/7za)

# Network Manager 
## 1. General Commands:
### List all NetworkManager connections:

```
nmcli con show
```

### Display general status of NetworkManager:
```
nmcli general status
```

### List available Wi-Fi networks:
```
nmcli device wifi list
```

## 2. Connecting to a Wi-Fi Network:
If you want to connect to a new Wi-Fi network:

### Connect to a network (if the network is open):
```
nmcli device wifi connect [SSID]
```

### Connect to a network with a password:
```
nmcli device wifi connect [SSID] password [PASSWORD]
```

Replace [SSID] with the name (SSID) of the network and [PASSWORD] with the network's password.

## 3. Managing Connections:
### Disconnect from a network:

```
nmcli device disconnect [INTERFACE]
```
Replace [INTERFACE] with the name of your network interface (e.g., wlan0).

### Delete a connection:

```
nmcli con delete [CONNECTION_NAME]
```
Replace [CONNECTION_NAME] with the name of the connection you want to delete.

## 4. Working with VPN:
If you use VPNs, nmcli can manage those connections as well.

### Start a VPN connection:

```
nmcli con up id [VPN_NAME]
```

### Stop a VPN connection:
```
nmcli con down id [VPN_NAME]
Replace [VPN_NAME] with the name of your VPN connection.
```

## 5. Other Utilities:
### Turn networking on/off:
```
nmcli networking on
nmcli networking off
```
### Turn Wi-Fi on/off:
```
nmcli radio wifi on
nmcli radio wifi off


