# Files structure
```
/myproject
│   ├── .gitignore
│   ├── run.py
│   ├── /env                  # virtual environment
│   ├── /app
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── /templates
│   │       └── home.html
```

# .gitignore
```
# .gitignore
__pycache__
*.py[cod]
.env
env/
```

# /run.py
```
from app import app
if __name__ == "__main__":
    app.run(debug=True, port=5001)
```

# /app/init.py
```
from flask import Flask
app = Flask(__name__)
from app import routes
```

# /app/routes.py
```
from flask import render_template
from app import app
@app.route('/')
def home():
    return render_template('home.html')
```

# /templates/home.html
```
<!-- templates/home.html -->
<!DOCTYPE html>
<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```


# Sample app

create file server.py
```
touch /home/project/server.py
```

server.py content:
```
from flask import Flask

app = Flask("Hello Word...")

@app.route("/")
def hello():
    return "Hello World!"

if __name__=="__main__":
    app.run(debug=True)
```

run app
```
python3 server.py
```

# Decorators
Allow to reuse code. E.g. decorateor for json
```
def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)

print(hello())
print(add())
```

The output of above will be
```
{'output': 'hellow world'}
Enter a number = 73
Enter another number - 87
{'output': 160}
```

# Additional functions
## Access Forma Data with flask.request.form
use in POST requests
```
<form method="POST" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Submit">
</form>
```

e.g. to access username and password
```
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here
```

## Redirect 
```
from flask import redirect

@app.route('/admin')
def admin():
    return redirect('/login')
```

## Generate dynamic urls with flask.url_for
```
from flask import url_for

@app.route('/admin')
def admin():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "<Login Page>"
```

## Handling different HTTP requests
```
@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # process POST request
    if request.method == 'GET':
        # process GET request
```

For this in HTML file allow GET and POST requests in form
```
<!-- For POST -->
<form method="POST" action="/data">
    <!-- Your input fields here -->
    <input type="submit" value="Submit">
</form>

<!-- For GET -->
<a href="/data">Fetch data</a>
```

# CRUD

## Create
HTTP form
```
<form method="POST" action="/create">
    <input type="text" name="name">
    <input type="submit" value="Create">
</form>
```

Python:
```
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Create a new record with the name
        record = create_new_record(name)  # Assuming you have this function defined
        # Redirect user to the new record
        return redirect(url_for('read', id=record.id))
    # Render the form for GET request
    return render_template('create.html')
```

## Read
```
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    # Get the record by id
    record = get_record(id)  # Assuming you have this function defined
    # Render a template with the record
    return render_template('read.html', record=record)
```

## Update

HTML:
```
<form method="POST" action="/update/{{record.id}}">
    <input type="text" name="name" value="{{record.name}}">
    <input type="submit" value="Update">
</form>
```

Python code:
```
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Update the record with the new name
        update_record(id, name)  # Assuming you have this function defined
        # Redirect user to the updated record
        return redirect(url_for('read', id=id))
    
    # Render the form for GET request with current data
    record = get_record(id)  # Assuming you have this function defined
    return render_template('update.html', record=record)
```

## Delete
HTML
```
<form method="POST" action="/delete/{{record.id}}">
    <input type="submit" value="Delete">
</form>
```

Python
```
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Delete the record
    delete_record(id)  # Assuming you have this function defined
    # Redirect user to the homepage
    return redirect(url_for('home'))
```







