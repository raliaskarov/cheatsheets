# Routes Example

Example how to organise API end points in different executions

## Javascript
### Query
```
const express = require('express');
const app = express();
const port = 3000;

// Sample data (same as your Python version)
const data = [
  {
    id: "3b58aade-8415-49dd-88db-8d7bce14932a",
    first_name: "Tanya",
    last_name: "Slad",
    graduation_year: 1996,
    address: "043 Heath Hill",
    city: "Dayton",
    zip: "45426",
    country: "United States",
    avatar: "http://dummyimage.com/139x100.png/cc0000/ffffff"
  },
  {
    id: "d64efd92-ca8e-40da-b234-47e6403eb167",
    first_name: "Ferdy",
    last_name: "Garrow",
    graduation_year: 1970,
    address: "10 Wayridge Terrace",
    city: "North Little Rock",
    zip: "72199",
    country: "United States",
    avatar: "http://dummyimage.com/148x100.png/dddddd/000000"
  },
  // ... more entries
];

app.get('/name_search', (req, res) => {
  const query = req.query.q;

  // Check if query is missing
  if (query === undefined) {
    return res.status(400).json({ message: "Query parameter 'q' is missing" });
  }

  // Check if query is empty or numeric
  if (query.trim() === "" || /^\d+$/.test(query)) {
    return res.status(422).json({ message: "Invalid input parameter" });
  }

  // Search for person by first name
  const person = data.find(p =>
    p.first_name.toLowerCase().includes(query.toLowerCase())
  );

  if (person) {
    return res.status(200).json(person);
  } else {
    return res.status(404).json({ message: "Person not found" });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});

```

## Python Flask
### Query
```
from flask import Flask, make_response, request

app = Flask(__name__)

# data

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@app.route('/')
def index():
    return ({"message: ": "Hello world!"}, 204)

@app.route('/index_explicit')
def index_explicit():
    resp = make_response({"Message: ": "Hello world"})
    resp.status_code = 204
    return resp

# checked if data in file
@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

# route to search by name
@app.route("/name_search")
def name_search():
    """ Find person in db

    returns:
        json: if found status 200
        404: if not found
        400: if arg is missing
        422: if arg is invalid
    """

    # get arg q from request
    query = request.args.get('q')

    # check if q is missing
    if query is None:
        return {"message": "Querry paramteter 'q' missing"}, 400

    # check is query is invalid
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input param"}, 422

    # iterate through data
    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    # if no match return 404
    return {"message": "person not found"}, 404
```
