
**Software management**

|-----------------|-------------------------------------|
|show intalled | ` $ yum list installed ` "

# update all
`$ sudo yum update`

#update 1 pack
$ sudo yum update openssl

#show installed repos
yum repolist all

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
