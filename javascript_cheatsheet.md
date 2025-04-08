# Basic commands and sample code blocks in JS
(C) IBM Coursera IBM Full Stack Developer Certificate

## Operators

## Variable
let vs var
let is block-scope
```
for (let i = 0; i < 3; i++) {
  console.log(i);
}
console.log(i); // ❌ ReferenceError: i is not defined

```

var is function scoped
```
for (var i = 0; i < 3; i++) {
  console.log(i);
}
console.log(i); // ✅ 3 — `i` is still accessible here!

```
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

### for loop

print 1 to 10 adding 4 to each value
```
let minVal = 1;
let maxVal = 10;

for (let i = minVal; i <= maxVal; i++) {
  console.log(i + 4); // Add 4 to each value
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
//Creates the element <p> and text "Hello World". Appends Hello World <p> to the HTML document.
<head>
 <script>
  function addPara() {
   var newPara = document.createElement("p");
   var newText = document.createTextNode("Hello World!");
   newPara.appendChild(newText);
   document.body.appendChild(newPara);
  }
 </script>
</head>
<body onload="addPara()">
</body>
```

**Arrays**
```
const Beatles = ["Ringo", "Paul", "George", "John"];
//Here Beatles[0] is "Ringo".
```


**Date()**
Create date from string
```
//create a new date from a string
var newDate = new Date("2021-1-17 13:15:30");

//create a new date instance representing 17 Jan 2021 00:00:00
//note that the month number is zero-based
var newDate = new Date(2021, 0, 17);

// get year
Date().getFullYear()
```
Assign current local date and time
```
var newDate = new Date();
```
**document.createElement()**
```
//Creates the element <p> and text "Hello World". Appends Hello World <p> to the HTML document.
<head>
 <script>
  function addPara() {
   var newPara = document.createElement("p");
   var newText = document.createTextNode("Hello World!");
   newPara.appendChild(newText);
   document.body.appendChild(newPara);
  }
 </script>
</head>
<body onload="addPara()">
</body>
```

**document.createTextNode()**
```
//Creates the element <p> and text "Hello World". Appends Hello World <p> to the HTML document.
<!DOCTYPE html>
<html>
    <head>
        <script>
            function addPara() {
                newPara = document.createElement('p');
                newText = document.createTextNode('Hello World!');
                newPara.appendChild(newText);
                document.body.appendChild(newPara);
            };
        </script>
        </head>
        <body onload='addPara()'>
        </body>
</html>
```

**document.getElementByID()**
```
//Changes the content of the div to "Hello World!"
<div id="div1">
 <p>Hello</p>
 <p>Hello</p>
</div>

<script>
 document.getElementById("div1").innerHTML = "<p>Hello World!</p>";
</script>
```

Change value of an element
```
<script>
function updateRate() {
    var rateval = document.getElementById("rate").value;  
    console.log("Received rate value", rateval)  
    document.getElementById("rateval").innerText = rateval
}
</script>

<br/>
Rate <input id="rate"
	type="range"  min="1" max="20" value="10.25" step="0.25"
	onchange="updateRate()"
	>
<span id="rateval">
10.25
</span>%<br/>

```

**document.getElementsByTagName()**
```
//Gets an array of all elements in a document with the <p> tag.
var tagNameArray = document.getElementsByTagName("p");
```

**document.write()**
```
//Writes "Hello World" to the output stream.
document.write("Hello World")
```


**element.getAttribute()**
```
 //Removes the CSS style color blue
<div id="div1" style="color: blue"></div>
<script>
 var div1 = document.getelementById("div1").getAttribute("style");
</script> 
```

**element.innerHTML()**
```
//Changes the content of the div to "Hello World!"
<div id="div1">
 <p>Hello</p>
 <p>Hello</p>
</div>

<script>
 document.getElementById("div1").innerHTML = "<p>Hello World!</p>";
</script>
```

**element.removeAttribute()**
```
//Removes the CSS style color blue
<div id="div1" style="color: blue"></div>
<script>
 var div1 = document.getelementById("div1").getAttribute("style");
</script>
```

**element.setAttribute()**
```
//In all elements named "theImage" sets the name of all src attributes to "another.gif"
document.getElementById("theImage").setAttribute("src", "another.gif");
```

**element.style()**
```
//Changes the CSS style color from blue to red
<div id="div1" style="color: blue"></div>
<script>
 var div1 = document.getelementById("div1");
 div1.style.color = "red";
</script>
```

**.this**
```
// Modify the code of the Car object directly to add a color parameter in the constructor
function Car(color) {
  this.color = color;
}
```

**Error Objects**
```
//Catch statement defines a block of code to be executed if an error occurs in the try block.
catch (err) {
 document.getElementById("myfile").innerHTML = err.name;
}
//Creates custom error message
throw new Error("Only values 1-10 are permitted");
```


**History Objects**
```
//Go back two pages if the history exists in the history list.
history.go(-2);
```

**insertBefore()**
```
//Creates a new <li> element and places it in the elementList before the first child of <ul>
let newLI = document.createElement("li");
newLI.innerText = "new Element";
let elementList = document.getElementById("thisList");
elementList.insertBefore(newLI, elementList.childNodes[0]);
```

**Location Objects**
```
//Returns the hostname property
let myhost = location.hostname;
newLI.innerText = "new Element";
```

**Navigator Objects**
```
//Retrieves the name of the browser
var browsername = navigator.appName;
```

**onload()**
```
//Executes myFunction after MyHTMLPage has been loaded
document.getElementById("MyHTMLPage").onload = function () {myFunction};
```

**replaceChild()**
```
//Creates a new node and replaces the second element in "thisList" with the word "blue"
let secondBullet = document.createTextNode("blue");
var myList = document.getElementById("thisList").childNodes[1];
myList.replaceChild(secondBullet,   myList.childNodes[1]);
```

**Screen Objects**
```
//Returns the height and width of the user’s screen
var height=screen.height;
var width=screen.width;
```

**Window Objects**
```
//Opens a new browser window with the specified URL
window.open("http://www.w3schools.com")
```


**window.open()**
```
//Opens a new window that opens the IBM home page and has a width of 600 and a height of 800)
let thisWindow = window.open("http://www.ibm.com", "myWindow", "width"=600, "height"=800);
```

**window.scrollTo()**
```
//Scrolls the window to the pixel located at the coordinate (20, 200)
window.scrollTo(20, 200);
```

**Wrapper Objects**
```
/Enables the use of properties and methods of the String class such as the property n.length
let n = new String ("abc");

//Returns string
typeof "abc";

//Returns object
typeof new String("abc");
```

convert number to string
```
num = 123
num.toString()
//or
String(num)
```

object vs primitive
```
var a = new String("Hello"); // a is a String object
var b = "Hello";             // b is a string primitive

if (a === b) {
  alert("Same");
} else {
  alert("Different"); // 👈 This is what runs
}

```

if you write 
```
"hello".toUpperCase
```
code will do in background
```
let temp = new String("hello"); // temporarily
temp.toUpperCase();

```

### Event Binders
```
<div onmouseover="console.log('hovering')">Hover me</div>
<button onclick="alert('Clicked!')">Click Me</button>
<body onload="init()">  
```

## Calculations
```
const I = 5
const p = 1000
var amount = parseInt(p) + parseFloat(I); // this returns 1005
var amount_concatenate = p + I; // this returns 10005
```


### Input fields
