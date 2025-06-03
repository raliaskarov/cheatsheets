# Python PEP8 standards and Static Code Analysis in PyLint

Install pylint
```
pip install pylint
```

Run static code analysis
```
pylint server.py
```

Example output:
```
$ pylint server.py
************* Module server
server.py:20:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
server.py:35:4: W0105: String statement has no effect (pointless-string-statement)

-----------------------------------
Your code has been rated at 8.75/10
```
