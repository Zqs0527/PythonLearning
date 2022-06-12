from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calculate_area(self):
        pass


class Book:
    def __init__(self, name, price, discount, chapters):
        self.name = name
        self.price = price
        self.discount = discount
        self.chapters = chapters

    
    def __getattribute__(self, __name: str):
        if __name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("discount")
            return p - p*d
        return super().__getattribute__(__name)
        

    def __setattr__(self, __name: str, __value):
        if __name == 'price':
            if type(__value) is not float:
                raise ValueError("The price must be float type")
        return super().__setattr__(__name, __value)

    def __str__(self) -> str:
        return f"Book name: {self.name}, price: {self.price}, number of chapters: {self.chapters}"

b1 = Book("Actie",50.0,0.5,56)
# b1.price = 30.9
print(b1)