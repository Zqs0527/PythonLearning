class Book:
    # it is called before other methods are called
    def __init__(self, title) -> None:
        self.title = title
class Newspaper:
    def __init__(self, name) -> None:
        self.name = name



b1 = Book("Three swans")
b2 = Book("Nederland in actie")
n1 = Newspaper("Daily")
n2 = Newspaper("Yearly")

print(type(b1))
print(type(n1))

print(type(b1) == type(b2))
print(type(b1) == type(n2))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
