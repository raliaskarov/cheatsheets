
**Software management**

|Command                              |Action                               |
|-------------------------------------|-------------------------------------|
|` $ yum list installed `| show intalled|
|`$ sudo yum update`|update all|
|`$ sudo yum update openssl`|update 1 pack|
|`yum repolist all`|show installed repos|

#find package
$ sudo yum search "find"

#add repo
sudo yum-config-manager --add-repo https://www.example.com/repository.repo

#install package
sudo yum install <PACKAGE>

**Files managmenet**
#remove EMPTY directory
rmdir <DIRECTORY>

#remove not empty directory with all contents
rm -r <DIRECTORY>

**Navigation**
#Print working directory
$ pwd

**Terminal multiplexer**

#close tmux session
tmux kill-session


**Working with pip**
sudo pip3 install -r requirements.txt
