## OOP Refreshing
- It is not required to create objects or classes
- Complex program
    - Groups data and behavior
    - Promotes modulization of programs
    - Isolates different parts of the programs

- Class: A blueprint for creating objects of a particular type
- Methods: Regular functions that are part of a class
- Attributes: Variables that hold data that are part of a class
- Object: A specific instance of a class
- Inheritance: Means by which a class cna inherit capabilities from another
- Composition: Means of building complex objects out of other objects

```
class Book(): # parenthese is not required, only if the class is inhenrited from another class
    self.__secret = "This is a secret"
```
Attributes with double underscores can't be accessed outside of the class. Prefixing the attribute name with the class name. This is called **name mangling**. This is prevent subclass inadvertently overriding the attribute, but other class can subvert simply by using the class name
```
b1 = Book()
print(b1._Book__secret)
```
### Static methods

- They don't modify the state of either the class or a specific object instance. It is useful when you don't need to access any properties of a particular object or the class itself. However, it makes sense the method belongs to the class

### Base class
`super().__init__()`
- Abstract base classes

`from abc import ABC, abstractmethod`

It is a very useful tool for setting constraints among the consumer of your classes

Method resolution order: The look up starts in the current class. 
```
class C (A, B)
```
Class A and class B have the same attribute. When the attribute is printed in using the instance of C, it will be the value of the attribute in class A.
```
C.__mro__
```
Above `__mro__` stands for method resolution order

### Python 'Magic' Methods
`def __str__()` method to return a string
`def __repr__` method to return an obj 
```
def __repr__(self):
    return f"title={self.title},name={self.name}"

print(repr(obj))
```
`def __eq__()` checks for the equality between two objects

`def __ge__()` establishes >= relationship with another obj

`def __lt__()` establishes <= relationship with another obj

`def __getattribute__(self, name)`
```
def __getattribute__(self, name):
    if name == 'price':
        property = super().__getattribute__('price')
        discount = super().__getattribute__('discount')
        return poperty - property*discount

    return name
```
Use `super().__getattribute__()` is to avoid recursion
