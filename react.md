Notes from my studies on react.

## What is lifecycle of a component?
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



## How to send data from Child to Parent?
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

## How to post data to server?
- Collect Data: It collects the data that needs to be sent to the server. This data could be user input from a form, information generated during the application's runtime, or any data that the application needs to persist beyond the current session.
- Initiate an HTTP Request: It uses an HTTP client (such as the Fetch API, Axios, or XMLHttpRequest in JavaScript) to send an HTTP request to the server. This request is typically a POST request when creating new resources or sending data for processing.
- Serialize Data: Before sending the data, it serializes the data into a format that the server can understand. JSON (JavaScript Object Notation) is a commonly used format for such data exchange.
- Handle the Response: After sending the data, it waits for a response from the server. The response could indicate success (e.g., HTTP status code 200 OK or 201 Created) or failure (e.g., 400 Bad Request, 500 Internal Server Error).
- Error Handling: It includes error handling mechanisms to deal with network issues, server errors, or any other problems that might occur during the data transmission.

```
async function postDataToServer(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

// Example usage:
postDataToServer('https://example.com/data', { key: 'value' })
  .then(data => {
    console.log(data); // JSON data parsed by `response.json()` call
  })
  .catch(error => {
    console.error('Error:', error);
  });

```
