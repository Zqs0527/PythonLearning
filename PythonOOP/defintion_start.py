#TODO: Create a basic class
from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE


class Book:
    # it is called before other methods are called
    def __init__(self, title, author, pages, price) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        #TODO: add properties
    
    #TODO: create instance methods
    def get_price(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, discount: float):
        self._discount = discount


#TODO: Create instances of the class
b1 = Book("Three swans","someone", 123, 67.8)
b2 = Book("Nederland in actie", "Tim", 34, 45)


#TODO: Print the class and property
print(b1)
print(b1.title)

#TODO: Get price of the book
print(b1.get_price())

#TODO: Try setting discount
b1.set_discount(0.23)
print(b1.get_price())