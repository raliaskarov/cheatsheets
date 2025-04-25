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
source /usr/share/nvm/init-nvm.shWhere in the callback function does a Node.js generally pass an error object?
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

### Url
get parts from URL:
urlDemo.js
```
const url = require('url');
let webAddress = 'http://localhost:2000/index.html?lastName=Kent&firstName=Clark';
let qry = url.parse(webAddress, true);
let qrydata = qry.query; //returns an object: {lastName: 'Kent', firstName: 'Clark'}
console.log(qrydata.firstName); //outputs Clark
console.log(qrydata);
```

### Querystring
Parse query (not whole url)
querystringDemo.js
```
let qry = require('querystring');
let qryParams = qry.parse('lastName=Kent&firstName=Clark');
console.log(qryParams.firstName); //returns Clark
```

# Package Manager
Local install
```
npm install <package_name>
```
Machine-wide install (global)
```
npm install -g <package_name>
```

### Import modules
**Import**
```
    // addTwoNos.mjs
    function addTwo(num) {
      return num + 4;
    }
    export { addTwo };
    // app.js
    import { addTwo } from './addTwoNos.mjs';
    // Prints: 8
    console.log(addTwo(4));
```

**Require**
The require() statement essentially reads and executes a JavaScript file before returning the export object. 
```
    module.exports = 'Hello Programmers';
    let msg = require('./messages.js');
    console.log(msg);
```

## Promises, Async/Await, Axios


### Promises

An object that is returned by some methods, representing eventual completion or failure is called promise. The code continues to run without getting blocked until the promise is fulfilled or an exception is thrown. 

Promise syntax
```
axios.get(url).then(
//do something
).catch(
//do something
)
```

Create promise
```
// Creating a new Promise object and assigning it to the variable myPromise
const myPromise = new Promise((resolve, reject) => {

  // Simulating a condition with a boolean variable 'success'
  let success = true; 

  // If the condition is true, call resolve to mark the promise as fulfilled
  if (success) { 
    resolve("The operation was successful!");
  } else { 
    // If the condition is false, call reject to mark the promise as rejected
    reject("The operation failed!");
  } 
});
```

Use .then() and .catch() to chain multiple asynchronous operations in sequence
```
// Execute the promise and handle the fulfilled and rejected states
myPromise

  // Handle the resolved state of the promise
  .then((message) => { 
    // This block will execute if the promise is resolved
    console.log(message); // "The operation was successful!"
  }) 

  // Handle the rejected state of the promise
  .catch((error) => { 
    // This block will execute if the promise is rejected
    console.error(error); // "The operation failed!"
  });
```

Example: read file with application of .then() and .catch()
```
// Import the 'fs' module and use its promise-based methods
const fs = require('fs').promises;

// Read the content of the file 'example.txt' with 'utf8' encoding
fs.readFile('example.txt', 'utf8')

  // Handle the resolved state of the promise
  .then((data) => { 
    // This block will execute if the file is read successfully
    console.log(data); // Print the file content to the console
  }) 

  // Handle the rejected state of the promise
  .catch((err) => { 
    // This block will execute if there is an error reading the file
    console.error('Error reading file:', err); // Print the error message to the console
  });
```

**Another example of promise use case**
Promises are used when the processing time of the function we invoke takes time like remote URL access, I/O operations file reading, etc. 
```
let prompt = require('prompt-sync')();
let fs = require('fs');
const methCall = new Promise((resolve,reject)=>{
    let filename = prompt('What is the name of the file ?');
    try {
      const data = fs.readFileSync(filename, {encoding:'utf8', flag:'r'});
      resolve(data);
    } catch(err) {
      reject(err)
    }
});
console.log(methCall);
methCall.then(
  (data) => console.log(data),
  (err) => console.log("Error reading file")
);
```

 
### Async and await**
**Async-await**
Wait for promise insite async function
```
const axios = require('axios').default;
let url = "some remote url"
async function asyncCall() {
  console.log('calling');
  const result = await axios.get(url);
  console.log(result.data);
}
asyncCall();
```

**Callback**
Callbacks are methods that are passed as parameters. They are invoked within the method to which they are passed as a parameter, conditionally or unconditionally. We use callbacks with a promise to process the response or errors. 
```
//function(res) and function(err) are the anonymous callback functions
axios.get(url).then(function(res) {
    console.log(res);
}).catch(function(err) {
    console.log(err)
})
```

Using async/await does same job as .then() and .catch() to sequence operations but code is easier to read
```
// Async function that wraps the operation
async function myAsyncFunction() {
  // Simulating a condition with a boolean variable 'success'
  let success = true;

  // If the condition is true, resolve with a success message
  if (success) {
    return "The operation was successful!";
  } else {
    // If the condition is false, throw an error to simulate rejection
    throw new Error("The operation failed!");
  }
}
// Using async function to handle Promise
async function executeAsyncFunction() {
  try {
    // Await the async function call to get the result
    const result = await myAsyncFunction();
    console.log(result); // Output the result if successful
  } catch (error) {
    console.error(error.message); // Handle and output any errors
  }
}

// Call the async function to execute
executeAsyncFunction();
```
** Promise vs Callback**
Both do same thing using different method
| Callback | Promise |
|:---|:---|
| Older method (classic Node.js style) | Newer method (ES6+ modern JavaScript) |
| Use a function passed as a parameter to handle the result | Use `.then()` and `.catch()` methods to handle success and failure |
| Can get messy if many async operations happen (called "callback hell") | Cleaner and easier to read, especially when chaining multiple async tasks |
| You have to manually check errors inside the callback | Errors automatically move to `.catch()` block |

**Synchronous vs callback vs Promise**
This is http request **without** callback/promise
```
const req = http.get('http://example.com');
req.on('response', (res) => {
    // Handle response
});

```
This is simple but will block code from further execution until response is received

This is same operation with **callback**
```
const http = require('http');

http.get('http://example.com', (res) => {
    // Optional callback
    res.on('data', (chunk) => {
        console.log(`Data chunk: ${chunk}`);
    });
});
What’s happening:

1. You send a GET request to http://example.com.
2. The request goes out over the network.
3. Meanwhile, Node.js keeps going — it doesn’t block.
4. Later, when the server responds, Node emits a response event.
5. Your callback (the one in .on('response', callback)) handles that event.

This is same operation but in modern way with **promise**
```
const axios = require('axios');

axios.get('http://example.com')
    .then(response => {
        console.log(response.data);
    })
    .catch(err => {
        console.error(err);
    });
```


**error parameter in callback and promise**
Callbacks: ```callback(err, data)``` → error is 1st parameter
Promises: ```.then(data).catch(err)``` → handled separately

### Axios
**--> The axios package** handles HTTP requests and returns a promise object. 
 
Install
```
npm install axios
```

Simple axios code
```
const axios = require('axios').default;
const connectToURL=(url)=>{
  const req=axios.get(url);
  console.log(req);
  req.then(resp=>{
  console.log("Fulfilled");
  console.log(resp.data);
  })
  .catch(err=>{
  console.log("Rejected");
  });
}
connectToURL('valid-url')
connectToURL('invalid-url')
```

**Make GET request**
```
// Import the axios library

const axios = require('axios');

// Using the axios.get method to make a GET request to the specified URL.

axios.get('https://api.example.com/data')

  // If the request is successful, the `.then` block is executed.

  .then(response => {
    // The response object contains the data returned from the server.
    // We log the `data` property of the response to the console.

    console.log(response.data);
  })

  // If there is an error during the request, the `.catch` block is executed.

  .catch(error => {
    
    // We log an error message to the console along with the error object.
    // This helps in debugging and understanding what went wrong with the request.
    
    console.error('Error fetching data:', error);
  });
```

**Make POST request**
```
// Import the axios library.

const axios = require('axios');

// Data to be sent in the POST request. This is a JavaScript object containing the user information.
const data = {
  name: 'John Doe',
  age: 30
};

// Using the axios.post method to make a POST request to the specified URL with the data object.
axios.post('https://api.example.com/users', data)
  
// If the request is successful, the `.then` block is executed.
  .then(response => {
    
// The response object contains the data returned from the server.
// We log a message along with the `data` property of the response to the console.
    
    console.log('User created:', response.data);
  })
  // If there is an error during the request, the `.catch` block is executed.
  
    .catch(error => {
    // We log an error message to the console along with the error object.
    // This helps in debugging and understanding what went wrong with the request.
    
    console.error('Error creating user:', error);
  });
```

**JSON**
Read JSON and parse to readable text
```
// Requiring axios module for making HTTP requests
const axios = require('axios').default;

// Sending a GET request to the specified URL using axios
const req = axios.get("https://raw.githubusercontent.com/ibm-developer-skills-network/lkpho-Cloud-applications-with-Node.js-and-React/master/CD220Labs/async_callback/courseDetails.json");
// Logging the initial promise object
console.log(req);
// Handling the promise resolution
req.then(resp => {
    // Storing the response data in the courseDetails variable
    let courseDetails = resp.data;
    // Logging the course details as a formatted JSON string
    console.log(JSON.stringify(courseDetails, null, 4));
})
// Handling the promise rejection
.catch(err => {
    // Logging the error message
    console.log(err.toString());
    // This will console log the error with the code. e.g., Error: Request failed with status code 404
});

```
Conversion to readable json done by ***JSON.stringify(courseDetails, null, 4)*** otherwise code would display OBJECT 

## Event handling
### Event handlers
**object.on()**
Identifies event handler called when event occurs
```
http.request( options, function(response) {
 let buffer = ``;
 ...
 response.on('data', function(chunk) {
   buffer += chunk;
 });
 response.on('end', function() {
   console.log(buffer);
 });
}).end();
```

## Don't dos
### List of situations to avoid
**Callback Hell a.k.a. Pyramid of Doom**
Nested callbacks stacked below one another
```
const makeCake = nextStep => {
  buyIngredients(function(shoppingList) {
    combineIngredients(bowl, mixer, function(ingredients){
      bakeCake(oven, pan, function(batter) {
        decorate(icing, function(cake) {
          nextStep(cake);
        });
      });
    });
  });
};
```
>> to make something to happen sequentially rather use ***async/await***





