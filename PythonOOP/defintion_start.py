#TODO: Create a basic class
class Book:
    # it is called before other methods are called
    def __init__(self, title) -> None:
        self.title = title


#TODO: Create instances of the class
b1 = Book("Three swans")
b2 = Book("Nederland in actie")


#TODO: Print the class and property
print(b1)
print(b1.title)