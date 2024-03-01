Notes from my studies on react.

# What is lifecycle of a component?
1. Mounting

In React, the function that is invoked right after a component is mounted on the DOM is componentDidMount for class components. This lifecycle method is used for class components to run code immediately after the component is inserted into the DOM, such as making API calls, adding event listeners, or doing any DOM manipulation.

Here's a simple example of how componentDidMount is used in a class component:
```
import React, { Component } from 'react';

class MyComponent extends Component {
  componentDidMount() {
    console.log('Component has been mounted on the DOM');
    // You can perform side-effects here, like fetching data or setting up subscriptions.
  }

  render() {
    return (
      <div>
        Hello, World!
      </div>
    );
  }
}

export default MyComponent;
```
For functional components, the useEffect hook with an empty dependency array [] serves a similar purpose as componentDidMount. It runs after the first render and is used for similar side effects as componentDidMount in class components. Here's how you might use it:
```
import React, { useEffect } from 'react';

function MyFunctionalComponent() {
  useEffect(() => {
    console.log('Component has been mounted on the DOM');
    // Perform side-effects here
  }, []); // The empty array means this effect runs once after the initial render

  return (
    <div>
      Hello, World!
    </div>
  );
}

export default MyFunctionalComponent;

```



# How to send data from Child to Parent?
To pass data from child components to parent components, you typically use a combination of callbacks and state. Here's a general approach:
- Define a Callback Function in the Parent Component: This function is responsible for updating the state in the parent component based on the data received from the child component.
- Pass the Callback Function as a Prop to the Child Component: The child component receives this function as a prop.
- Invoke the Callback Function from the Child Component: When an event occurs or data needs to be sent to the parent component, the child component calls the callback function, passing the necessary data as arguments.
- State Update in the Parent Component: The callback function in the parent component uses the passed data to update its state. This change in state can then be passed down to child components as props, if needed, creating a reactive data flow.
Example: the ParentComponent defines a function handleDataFromChild that updates its state. It passes this function to the ChildComponent as a prop called sendDataToParent. When a button in the ChildComponent is clicked, it invokes sendDataToParent, effectively sending data back to the ParentComponent and updating its state.

**Parent component**
```
import React, { useState } from 'react';
import ChildComponent from './ChildComponent';

function ParentComponent() {
  const [parentData, setParentData] = useState('');

  const handleDataFromChild = (dataFromChild) => {
    setParentData(dataFromChild);
  };

  return (
    <div>
      <h1>Data from Child: {parentData}</h1>
      <ChildComponent sendDataToParent={handleDataFromChild} />
    </div>
  );
}

export default ParentComponent;

```
**Child component**
```
import React from 'react';

function ChildComponent({ sendDataToParent }) {
  const sendData = () => {
    sendDataToParent('Data from Child');
  };

  return (
    <button onClick={sendData}>Send Data to Parent</button>
  );
}

export default ChildComponent;

```
