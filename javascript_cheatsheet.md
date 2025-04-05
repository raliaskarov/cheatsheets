# Basic commands and sample code blocks in JS
(C) IBM Coursera IBM Full Stack Developer Certificate

## Operators

### Assignment operators
```
= operator is used to assign value on the right to the variable on left
	+= operator is used to increment the value stored in the left operand by the value of the right operand and store it back to the left operand (the same as writing tmp = tmp + val where tmp is a variable and val is some arbitrary value)
	-= operator is used to decrement the value stored in the left operand by the value of the right operand and store it back to the left operand (the same as writing tmp = tmp - val where tmp is a variable and val is some arbitrary value)
	*= operator is used to multiply the value stored in the left operand by the value of the right operand and store it back to the left operand (the same as writing tmp = tmp * val where tmp is a variable and val is some arbitrary value)
	/= operator is used to divide the value stored in the left operand by the value of the right operand and store it back to the left operand (the same as writing tmp = tmp / val where tmp is a variable and val is some arbitrary value)
	**= operator is used to raise the value stored in the left operand to the power value of the right operand and store it back to the left operand (the same as writing tmp = tmp ** val where tmp is a variable and val is some arbitrary value)
	%= operator is used to get modulus of the value stored in the left operand by value of the right operand and store it back to the left operand (the same as writing tmp = tmp % val where tmp is a variable and val is some arbitrary value)
```

### Comparison operators

```
	== operator checks if the operand on the left is of equal value to the operand on right
	=== operator checks if the operand on the left is of equal value and equal type to the operand on right
	!= operator checks if the operand on the left is not of equal value to the operand on right
	> operator checks if the operand on the left is greater than that on the right
	< operator checks if the operand on the left is lesser than that on the right
	>= operator checks if the operand on the left is greater than or equal to that on the right
	<= operator checks if the operand on the left is lesser than or equal to that on the right
```

### Logical operators
```
	&& operator checks if the condition on left and right are true. Returns true only of both conditions are true. Else returns false.
	|| operators checked if either the condition on the left is true or right is true. Returns true even if one of the two conditions is true.
	! operator checks if the condition is not met.
```

### If statement
```
//Accept a input from the user. If it is a number, print the multiplication table for the number. Else print the input and the length of the input.
let user_input = prompt('Enter a value');
//Check if the user did not input anything
if (!user_input) {
	console.log("You did not input anything")
}
//Check if the user input is not a number
else if (isNaN(user_input)) {
	console.log("Your input is ", user_input)
	console.log("The length of your input is ", user_input.length)
}
//The only option remaining is that the input is a number
else {
	console.log(user_input, " X 1 = ", user_input*1)
	console.log(user_input, " X 2 = ", user_input*2)
	console.log(user_input, " X 3 = ", user_input*3)
	console.log(user_input, " X 4 = ", user_input*4)
	console.log(user_input, " X 5 = ", user_input*5)
	console.log(user_input, " X 6 = ", user_input*6)
	console.log(user_input, " X 7 = ", user_input*7)
	console.log(user_input, " X 8 = ", user_input*8)
	console.log(user_input, " X 9 = ", user_input*9)
	console.log(user_input, " X 10 = ", user_input*10)
}
```

### Switch operator
```
let user_input = prompt('Enter a number between 1 to 7');

//Using logical OR operator to check if the input is a number and it is between 1 to 7
if(isNaN(user_input) || user_input< 1 || user_input>7) {
	console.log("Invalid input")
} else {
	user_input = parseInt(user_input)
	switch(user_input){
    	case 1: console.log("Sunday"); break;
    	case 2: console.log("Monday"); break;
    	case 3: console.log("Tuesday"); break;
    	case 4: console.log("Wednesday"); break;
    	case 5: console.log("Thursday"); break;
    	case 6: console.log("Friday"); break;
    	case 7: console.log("Saturday"); break;
    	default: console.log("Invalid entry");
	}
}
```

### While statement
```
//The code below is to find the length of the words the user is entering. The loop will go on and on until the user chooses not to continue by pressing 'n'

let do_more = true

while(do_more) {
	//Accept a input from the user.
	let user_input = prompt('Enter a word');
	//Check if the user input is not a number and then print the length of the input
	if(isNaN(user_input)) {
    	console.log("Length of the word you entered is " + user_input.length)
	} else {
    	console.log("You entered a number. Only words are allowed")
	}
	let should_continue = prompt("Do you want to continue. Press n to stop")
    
	if(should_continue === "n") {
    	do_more = false
	}
}
```

### Functions
#### Calculate total sales
```
const sales = [
	{ item: "Laptop", quantity: 2, price: 800 },
	{ item: "Monitor", quantity: 1, price: 150 },
	{ item: "Mouse", quantity: 4, price: 25 }
];

function calculateTotalSales(sales) {
	let total = 0;
	for (let i = 0; i < sales.length; i++) {
    	total += sales[i].quantity * sales[i].price;
	}
	return total;
}

console.log("Total Sales Amount:", calculateTotalSales(sales));
```

#### Print receipt

```
const orders = [
	{ item: "Espresso", quantity: 2, price: 3.5 },
	{ item: "Latte", quantity: 3, price: 4.0 },
	{ item: "Cappuccino", quantity: 1, price: 4.5 }
];

function generateReceipt(orders) {
	let grandTotal = 0;
	console.log("Receipt:");
	console.log("----------------------");
	for (let i = 0; i < orders.length; i++) {
    	const itemTotal = orders[i].quantity * orders[i].price;
    	grandTotal += itemTotal;
    	console.log(`${orders[i].item} - Quantity: ${orders[i].quantity}, Price: $${orders[i].price}, Total: $${itemTotal}`);
	}
	console.log("----------------------");
	console.log(`Grand Total: $${grandTotal}`);
}

generateReceipt(orders);
```

#### Validate passwords
```
const passwords = ["Password123", "short", "ValidPass123", "too_long_password_example", "12345"];

function validatePasswords(passwords) {
    const regex = /^[a-zA-Z0-9]{8,20}$/;
    for (let i = 0; i < passwords.length; i++) {
        if (regex.test(passwords[i])) {
            console.log(`${passwords[i]} is valid.`);
        } else {
            console.log(`${passwords[i]} is invalid.`);
        }
    }
}

validatePasswords(passwords);
```

#### Track product stock level
```
const products = [
    { product: "Laptop", stock: 5 },
    { product: "Headphones", stock: 0 },
    { product: "Smartphone", stock: 3 }
];

function checkStockLevels(products) {
    for (let i = 0; i < products.length; i++) {
        if (products[i].stock > 0) {
            console.log(`${products[i].product} is In Stock.`);
        } else {
            console.log(`${products[i].product} is Out of Stock.`);
        }
    }
}

checkStockLevels(products);
```


### JS Blocks

**appendChild()**
```
//Creates the element <p> and text “Hello World”. Appends Hello World <p> to the HTML document.
<head>
 <script>
  function addPara() {
   var newPara = document.createElement(“p”);
   var newText = document.createTextNode(“Hello World!”);
   newPara.appendChild(newText);
   document.body.appendChild(newPara);
  }
 </script>
</head>
<body onload=“addPara()”>
</body>
```

**Arrays**
```
const Beatles = [“Ringo”, “Paul”, “George”, “John”];
//Here Beatles[0] is “Ringo”.
```


**Date()**
Create date from string
```
//create a new date from a string
var newDate = new Date(“2021-1-17 13:15:30”);

//create a new date instance representing 17 Jan 2021 00:00:00
//note that the month number is zero-based
var newDate = new Date(2021, 0, 17);
```

**document.createElement()**
```
//Creates the element <p> and text “Hello World”. Appends Hello World <p> to the HTML document.
<head>
 <script>
  function addPara() {
   var newPara = document.createElement(“p”);
   var newText = document.createTextNode(“Hello World!”);
   newPara.appendChild(newText);
   document.body.appendChild(newPara);
  }
 </script>
</head>
<body onload=“addPara()”>
</body>
```

**document.createTextNode()**
```
//Creates the element <p> and text “Hello World”. Appends Hello World <p> to the HTML document.
<head>
 <script>
  function addPara() {
   var newPara = document.createElement(“p”);
   var newText = document.createTextNode(“Hello World!”);
   newPara.appendChild(newText);
   document.body.appendChild(newPara);
  }
 </script>
</head>
<body onload=“addPara()”>
</body>
```
