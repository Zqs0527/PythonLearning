## Functions
All functions return a value
- In python, it is a **call-by-value** language. It is not passed by the object.
```
def main():
    x = 5
    kitten(x)
    printf(f'in main x is {x}')
def kitten(a):
    a = 3
    print('Meow')
    print(a)
```
After calling above `main()` function, the output is
```
Meow
3
in main x is 5
```
If the variable is passed by the object, if the value is changed in the function, the value outside is also changed. 

Integer is an immutable object. List is a muttable object.
```
x = [5]
y = x
y[0] = 3
```
If print x and y after above lines, x and y will both have value of 3. This is because `y=x` means y is pointing to the address of x.

Variadic arguments
- `*args`: list of arguments, a tuple of inputs
- `**kwargs`: list of arguments, a dictionary of inputs

### Generator
It is served as an iterator. Instead of returning a single value, it returns a stream of values
```
# generator
i = start
while i <= stop:
    yield i
    i += step
```
```
def generator(start,stop):
    while (start<=stop):
        yield start
        print(f'start={start}')
        start+=1
for counter in generator(3,4):
    print(f'counter={counter}')

The answer is:
counter=3
start=3
counter=4
start=4
```

### Decorator
It is a form of metaprogramming and it can be described as a special type of function that returns a wrapper function

```
def f1():
    def f2():
        print('this is f2')
    return f2
x = f1
x()
```
A function is also an object. In order to call f2, you should call f1, because f1 returns an object of f2. Here f1 is the wrapper of f2.

```
f3 = f1(f3)
f3()
```
f3 in its original form is no longer available

Decorator, it takes the function which is defined directly after it. Following function will becomes the argument of the decorator function. It returns and assigns that name of f3

## Structured data
- List
```
game = ['name','age','year','boy']

game[start:end:step]

i = game.index('name')

game.append('position')

game.insert(0, 'play')

```
game.pop() is to pop the last item
- Set

`-` can be used to check if elements in one set but not in the other set

`|` in one set or the other set or in both

`^` XOR
- List comprehension

```
from math import pi
[x for x in seq if x%3==0]
{x for x in 'appliepie' if x not in 'pd'}
```
- Misxed structure

## Class
First argument is `self`, it is reference to the object. `.` is used to dereference the methods in the class.

An instance of class is called an object. It is calling the class like a function. 

Constructor
```
x = [1,2,3]
def __init__(self, type, name, sound):
    self._type = type
    self._name = name
    self._sound = sound

def type(self):
    return self._type
```
In above lines, `self._type` is the object variable. `x` is the class variable. `x` is not encapsulated. It is not suggested to put a mutable data in a class.

A variable with an underscore is considered as a private variable, in python this is not true, but for good practice, use an underscore to indicate that the variable is not accessable.