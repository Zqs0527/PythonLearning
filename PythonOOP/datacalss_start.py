from dataclasses import dataclass, field


@dataclass
class Book:
    title: str = "No title"
    author: str = "no author"
    pages: int = 0
    price: float = field(default=0.0)

    def __post_init__(self):
        self.description = f"{self.title} is written by {self.author}"


b1 = Book('War', 'You', 45, 6.8)
b3 = Book('War', 'You', 45, 6.8)
print(b1.description)
print(b1.title)
print(b1)
print(b1==b3)
