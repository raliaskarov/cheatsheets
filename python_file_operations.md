#  Python file operations

Set of common commands to operate files in python


**Write paragraph to file**

```
text = "This is line 1\nThis is line 2\nThis is line 3"
with open("Example1.txt", "w") as file:
    file.write(text)
```

**Read content from file**
```
with open("Example1.txt","r") as file1: 

     FileContent=file1.read() 


print(FileContent) 
```
Output:
This is line 1

This is line 2

This is line 3

**Append text to file**
```
with open("Example.txt","w") as writefile: 

    writefile.write("This is line A\n") 

    writefile.write("This is line B\n")
```
