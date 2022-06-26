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

Binding the name to the object

It is possible to have multiple names for the same object. 
```
class shirts:
    def __init__(self):
        self.clean = True
    
    def make_clean(self):
        self.clean = True
    
    def make_dirty(self):
        self.clean = False
```
`red_shirts = shirts()`

`crimson_shirts = red_shirts`

Here `crimson_shirts` and `red_shirts` are referring to the same object. If the attributes of the `crimson_shirts` changed, the attributes of the `red_shirts` will also change