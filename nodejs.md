# Node JS Notes
My notes from node JS studies

## Installation
### Archlinux
```
sudo pacman -S nodejs
sudo pacman -S nvm
```
ensure that nvm loaded every time console is opened
```
source /usr/share/nvm/init-nvm.sh
```
also load it now
```
source ~/.bashrc
```


## Core modules

### Web Server
server.js
```
let http = require('http');

http.createServer(function (req, res) {
    res.write('hello from server'); // write a response to the client
    res.end(); // end of response from server
}).listen(3000); // server listens on port 6000
```
run:
```
node server.js
```
visit http://localhost:3000
