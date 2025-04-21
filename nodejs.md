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

To execute run:
```
node server.js
```
visit http://localhost:3000

### File System
**Read file, async**
readfile.js
```
const fs = require('fs');
// Asynchronously read the file 'sample.txt'
fs.readFile('sample.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    // Print the contents of 'sample.txt' to the console
    console.log(data);
});
```
**Read file, sync**
readFileSyncDemo.js
```
const fs = require('fs');
// Read the contents of the file '/content.md' synchronously and store them in 'data'
const data = fs.readFileSync('content.md', 'utf8');
// Print the contents of 'content.md' to the console
console.log(data);
```

### OS
Get operating system and architecture
getOsDemo.js
```
let os = require('os');
console.log("Computer OS Platform Info : " + os.platform());
console.log("Computer OS Architecture Info: " + os.arch());
```

### Path
This will return home.html
pathDemo.js
```
const path = require('path');
let result = path.basename('/content/index/home.html');
console.log(result); //outputs home.html to the console
```

### Util
Use to debug e.g. print to console iteration through loop
This will place i to placeholder %d (similar to python print(f"Priting text {i} now") function
utilDemo.js
```
let util = require('util');
let str = 'The loop has executed %d time(s).';
for (let i = 1; i <= 10; i++) {
    console.log(util.format(str, i)); //outputs 'The loop has executed i time(s)'
}
```
Returns:
The loop has executed 1 time(s).
The loop has executed 2 time(s).
The loop has executed 3 time(s).
The loop has executed 4 time(s).
The loop has executed 5 time(s).
The loop has executed 6 time(s).
The loop has executed 7 time(s).
The loop has executed 8 time(s).
The loop has executed 9 time(s).
The loop has executed 10 time(s).

Note: this can be executed without util but engine internally will use util anyway.
