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