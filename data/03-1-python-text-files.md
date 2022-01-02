# Data 3-1: Python - Text Files

### Writing a text file

This snippet opens a file in write mode and writes the word 'hello' with a newline character at the end.

```python
with open('testwrite.txt', 'w') as f:
    f.write('hello, this is a test file')
    f.write('\n')
```

`with open(...) as f` is called a "context manager". After opening a file, we generally want to close it to prevent memory leaks. The context manager will do this for us.

In this case we've opened the file in the context manager in write mode (`w`). You can append to the end of a file by opening it in the mode `a` like `with open('testwrite.txt', 'a') as f:`.

### Opening a text file

This snippet opens a file in read only mode (default), loads the entire contents of the file as a string in `full_text` and prints it out.

```python
with open('testwrite.txt') as f:
    full_text = f.read()

print(full_text)
```


### ❇️ Try It

Create a file called `name.txt` with your full name in it.

Write a python script called `readwrite.py` that:

1. reads `name.txt` into a variable `my_name` and then
2. writes a new file named `output/hello.txt` with the contents `Hello, my name is <my_name>.`
