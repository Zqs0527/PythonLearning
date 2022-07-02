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

Immutable and mutable data type. `string` type object is immutable. If one is changing the content of the string, there will be a `string` object created. It is not like a `list` type object

The child class can override the method which is inherited from the parent class.

`import random` is to import the entire module

`from random import randint` this will only import the `randint` method

To avoid the possible conflicts, the name of the modules can be renamed by calling `import random as rand`

Modules & Packages
- Module: Single python scripts which contain handful functions and classes relavent to the same type of task
- Package: It contains several modules

Multidimensional lists
```
a = [[1,2,3],[2,3,4]]
```
`a` is a 2x3 matrix

Queues are operating on first in first out (FIFO). 
- If one is calling on an empty queue, the program will wait until the method completes before continuing execution -> Blocking method
- Blocking works well when multiple threads or processes use queues to share information
    - `get(false)`: let user know the queue is empty

Stacks are operating on last in first out (LIFO)

Dictionary -> Hash Table 

`hash(key)`

Reverse lookup issues for dictionaries
```
def caller_id(lookup_number):
    for name,num in rolodex.items():
        if num == lookup_number:
            return name
```
There is no order defined in the dictionary