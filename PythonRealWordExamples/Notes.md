Benefits of functions
- Shorter programs - code can be used over and over
- More robust - less room to make mistakes
- Reuse code for similar tasks, change the code at one place

Parameter
- Variable name used inside of the function to access input passed to the function
- Input parameters. Must be uniquely 
- Asterisk in front of the parameter tells python that there might be any number of arguments when the function is called
```
def fancy_omelette(*ingredients):
    pass
```
`*ingredients` will be a tuple made of arguments

Argument
- The value passed to the function

Functions search for variables locally first. If the variable is not in the local scope, it expands the search to the global scope.

`dir('some string')` gives a list of attributes and methods which can be used