What is standard library?

- A library that can be used on any machine where you have an application using the specific language
- Built-in functions
- Imported cd repo  

`isinstance()` can be used to check if the object is an instance of a class. If the object is, then we can use certain functions from that class. `isinstance` is taken inheritance into consideration

math module to get GCD (greatest common denominator)

`random.sample(range(100), 5)` get 5 unique numbers from [0,99)

`random.choice(['cat', 'dog', 'tiger'])` returns a random choice from the given collection

`itertools` module can used to calculate the permutations and combinations

The usage:
```
election = {1: 'Bob', 2:'Karen', 3:'Erin'}
for p in itertools.permutations(election.values()):
    print(p)
```