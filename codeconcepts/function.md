#  Functions

## Setup

### Install python if you haven't already

macOS

```
brew install python
```

Ubuntu 

```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```

### Install node if you haven't already

Mac

```
brew install node
```

Ubuntu 

```
sudo apt-get install nodejs
```

## Defining a function

A function has inputs and an output. The inputs are known as the "arguments", and the output is known as a "return value"

![](https://www.evernote.com/shard/s150/sh/95140bf5-b70e-4fba-93a6-cde487903396/b15f7bf528929e3b/res/51b5407f-b640-4e9a-9c06-4da9f9ada4b4/skitch.jpg?resizeSmall&width=832)

below is an example of a function in python

```python
def multiply(a,b):
    return a * b
```

this is an example of the same function in  javascript

```javascript
function multiply(a,b) { 
    return a * b
}
```

This function takes two arguments (a and b), and returns the value of them multiplied together

![](https://www.evernote.com/shard/s150/sh/9aebfc82-14c3-45db-89d7-d1c5eecc37ba/5a8e9b0d30cdcd0d/res/cc48bfa7-e4e2-449f-8177-a1a9774a13aa/skitch.jpg?resizeSmall&width=832)


##  Calling a function

In the above exercise you have simply defined a function, but you haven't asked python to call it. If you ran the program above, you wouldn't see any output in the terminal.

```python
# This part of the code defines a function
def multiply(a,b):
    return a * b

# This part of the code then calls that function and assigns the variable x to its return value
x = multiply(8,9)

# This prints x to the terminal for humans to read
print(x)
```

in JavaScript that would look like this

```javascript
// This part of the code defines a function
function multiply(a,b) { 
    return a * b
}

// This part of the code then calls that function and assigns the variable x to its return value
var x = multiply(8,9)

// This prints x to the terminal for humans to read
console.log(x)
```

## Return vs Print

The function can also contain other logic and do other things. For example, you could write the function above like this:

```python
def multiply(a,b):
    print("I'm multiplying two numbers")
    return a * b
```

This would both print to the terminal and return a value. The return is the very last logical thing that happens in the execution of a function. Once a `return` is called, no additional code can be run inside the function. The same is true in JavaScript (and all programming languages).

## ➡️ Try It

