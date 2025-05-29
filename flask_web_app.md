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
Allo to reuse code. E.g. decorateor for json
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
