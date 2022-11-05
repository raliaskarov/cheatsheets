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
|` $ tmux kill-session`|close tmux session|
