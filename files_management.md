# Files managmenet with python

## Open()

Create file:

```
with open("myfile.txt", "w") as file:
    text = "line1: abc\nline2: cde"
    file.write(text)
```

Read first 2 lines:
```
with open("myfile.txt", "r") as file1:
    for n in range (0, 2):
        print(file1.readline())
```
