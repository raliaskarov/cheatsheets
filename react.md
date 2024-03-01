Notes from my studies on react.


# Sendign data from Child to Parent
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
