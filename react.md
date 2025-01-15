# React Commands

## Start app
install dependencies
```
npm install --verbose
```
** run script from package.json
```
npm run preview
```

# Code
## Default components
footer
```
    import React from 'react';
    const Footer = () => {
            return (
        <>
        </>
    )}

export default Footer
```

## Basic apps
counter
```
import React, { useState } from 'react';

function App() {
 const [count, setCount] = useState(0);

 return (
   <div>
     <h1>Counter: {count}</h1>
     <button onClick={() => setCount(count + 1)}>Increment</button>
   </div>
 );
}

export default App;
```
