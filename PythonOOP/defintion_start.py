#TODO: Create a basic class


class Book:
    #TODO: Proterties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")

    #TODO: Create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    #TODO: Double underscore properties

    #TODO: Create a static method

    # it is called before other methods are called
    def __init__(self, title, author, pages, price, book_type) -> None:
        self.title = title
        #TODO: add properties
        if (not book_type in Book.BOOK_TYPES):
            raise ValueError(f"{book_type} is not a valid book type")
        else:
            self.book_type = book_type
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"
    
    #TODO: create instance methods
    def get_price(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, discount: float):
        # _discount is designed to be only used by the class
        self._discount = discount

#TODO: Access to class attributes
print(Book.get_book_types())


#TODO: Create instances of the class
b1 = Book("Three swans","someone", 123, 67.8, "EBOOK")
b2 = Book("Nederland in actie", "Tim", 34, 45, "HARDCOVER")


#TODO: Print the class and property
print(b1)
print(b1.title)

#TODO: Get price of the book
print(b1.get_price())

#TODO: Try setting discount
b1.set_discount(0.23)
print(b1.get_price())

#TODO: Properties with double undescores are hidden by the interpreter
# By prefixing the class
print(b1._Book__secret)