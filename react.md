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
disable ssl checks
```
npm config set strict-ssl false
```

# Resources
React boilerplate
https://github.com/boilertown/react-ui-boilerplate

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

### Function Component with function keyword
Function component starts with function keyword along with name of the component and includes html tags within return. It also exports component name by default
```
import React from 'react'

function Extra() {
  return (
    <>
    <p>This is paragraph</p>
    </>
  )
}

export default Extra
```
### Function Component with arrow function
Function component starts with variable type along with name of the component and includes html tags within return. It also exports component name by default
```
import React from 'react'

const Extra = () => {
  return (
    <div>Extra</div>
  )
}

export default Extra
```
### Props in function component
Props can be sent from parent component as attribute along with child component
```
import React from 'react'
import ChildComponent from './ChildComponent'

function ParentComponent () {
    let title='Project Manager';
    return (
    <>
    <ChildComponent title={title}/>
    </>
  )
}
export default ParentComponent
```
### Access Props within child function component
rops can be accessed easily within the child function component using props.variable_name
```
import React from 'react'

const ChildComponent = (props) => {
  return (
    <>
    <p>The title is {props.title}</p>
    </>
  )
}

export default ChildComponent
```
### Event handling in class component
Events such as click event can be performed by calling function which is declared before return of function component
import React from 'react'
const Extra = (props) => {
    function show(){
        console.log('Show function');
    }
  return (
    <>
    <p>The title is {props.title}</p>
    <button onClick={()=>show()}>Click Here</button>
    </>
  )
}
export default Extra
### State management in function component
State management can be done easily with useState() hook
```
import React, { useState } from 'react'

const StateManagement = () => {
    const[name,setName]=useState('John');
  return (
   <>
   <h1>State Management using useState</h1>
    <p>The name is {name}</p>
   </>
  )
}
export default StateManagement
```
### Array Declaration
Array can be declared in square brackets
```
const names = ['Alice', 'Bob', 'Charlie'];
```
Stateful Array
```
const [todos, setTodos] = useState(['Learn React', 'Build Project']);
```
Dynamically Constructed Arrays
Arrays can be constructed dynamically based on application logic or received data
```
const numbers = [];
for (let i = 0; i < 10; i++) {
  numbers.push(i);
}
```
### Array map() method
The map() method is commonly used to iterate over each element of an array and return a new array of React elements
```
const items = ['Apple', 'Banana', 'Orange'];
const itemList = items.map((item, index) => <li key={index}>{item}</li>);
return <ul>{itemList}</ul>;
```
### for...of Loop
Use to  iterate over the elements of an array:
```
const items = ['Apple', 'Banana', 'Orange'];
for (const item of items) {
  console.log(item);
}
```
### Rendering a List of Items
You can render a list of items by mapping over an array and returning a JSX element for each item
```
import React from 'react';
function ArrayComponent() {
  const items = ['Autumn', 'Spring', 'Summer','Winter'];
  return (
    <div>
      <h1> Seasons Names</h1>
      <ul>
        {items.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
  </ul>
    </div>
  );
}
export default ArrayComponent;
```
### Adding and removing items in array
```
import React, { useState } from 'react';
function MyComponent() {
  const [items, setItems] = useState([‘Autumn’, ‘Spring’, ‘Winter’,’Summer’]);
  const [inputValue, setInputValue] = useState('');

  const addItem = () => {
    setItems([...items, inputValue]);
    setInputValue('');
  };

  const removeItem = (index) => {
    const newItems = [...items];
    newItems.splice(index, 1);
    setItems(newItems);
  };

  return (
    <div>
      <h1>Fruits</h1>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            {item}
            <button onClick={() => removeItem(index)}>Remove</button>
          </li>
        ))}
      </ul>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
      />
      <button onClick={addItem}>Add</button>
    </div>
  );
}
```
### Conditional rendering using ternary operator
You can conditionally render components based on the content of an array
```
import React, { useState } from 'react';

function ArrayComponent() {
    const [items, setItems] = useState(['React JS','Vue JS','Angular JS','Vanilla JS']);
  return (
    <div>
      <h1>Front End Languages</h1>
      {items.length > 0 ? (
        <ul>
          {items.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      ) : (
        <p>No Front End language is available</p>
      )}
    </div>
  );
}
export default ArrayComponent;
```
inline style in react
Inline style can be applied within the tag as an attribute within double curly braces
```
import React from 'react';
function MyComponent() {
  return (
    <div style={{ backgroundColor: 'lightblue', padding: '20px', borderRadius: '5px' }}>
      <p style={{ color: 'white', fontSize: '18px' }}>This is a paragraph with inline styles.</p>
    </div>
  );
}
export default MyComponent;
```
### Style using object
Style can be applied as an object like inline style
```
import React, { useState } from 'react';
function ToggleMessage() {
  const [isVisible, setIsVisible] = useState(true);
  const toggleVisibility = () => {
    setIsVisible(!isVisible);
  };
  const messageStyle = {
    display: isVisible ? 'block' : 'none',
    color: 'green',
    fontSize: '18px',
    marginTop: '10px'
  };
  return (
    <div>
      <h2>Toggle Message</h2>
      <button onClick={toggleVisibility}>
        {isVisible ? 'Hide Message' : 'Show Message'}
      </button>
      <p style={messageStyle}>This is a hidden message.</p>
    </div>
  );
}
```

## Arrays

|Method	|Returns New Array?	|Mutates Original Array?	|Common Use Case|
|---------| ---------|---------|-------------------------------|
|filter()	|Yes	|No	|Filtering out unwanted elements|
|map()	| Yes	|No	|Transforming each element in some manner|
|slice()	|Yes	|No	|Creating copies or subarrays|
|splice()	|No (returns removed elements)	|Yes	|In-place insert, remove, or replace elements|

**array.filter()**
```
const numbers = [1, 2, 3, 4, 5];
const evenNumbers = numbers.filter(num => num % 2 === 0);

console.log(evenNumbers); // [2, 4]
console.log(numbers);     // [1, 2, 3, 4, 5] (unchanged)
```
**array.map()**
```
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);

console.log(doubled); // [2, 4, 6]
console.log(numbers); // [1, 2, 3] (unchanged)
```
**array.slice()**
```
const fruits = ['apple', 'banana', 'cherry', 'date'];
const slicedFruits = fruits.slice(1, 3);

console.log(slicedFruits); // ['banana', 'cherry'] (indexes 1, 2)
console.log(fruits);       // ['apple', 'banana', 'cherry', 'date'] (unchanged)
```
**array.splice()**

* remove
```
const fruits = ['apple', 'banana', 'cherry', 'date'];
const removed = fruits.splice(1, 2); 
// Removes 2 elements starting at index 1

console.log(removed);  // ['banana', 'cherry']
console.log(fruits);   // ['apple', 'date'] (mutated!)
```
* insert
```
const colors = ['red', 'blue'];
colors.splice(1, 0, 'green', 'yellow'); 
// Insert 'green', 'yellow' at index 1, removing 0 elements

console.log(colors); 
// ['red', 'green', 'yellow', 'blue'] (mutated)
```
* replace
```
const animals = ['cat', 'dog', 'bird'];
animals.splice(1, 1, 'fish');
// At index 1, remove 1 element ('dog'), and insert 'fish'

console.log(animals); // ['cat', 'fish', 'bird']
```
