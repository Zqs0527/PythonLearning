class Duck:
    sound = 'Quack, quack'
    movement = 'Walks like a duck'

    # initializer ot constructor
    def __init__(self, **kwargs) -> None:
        pass
    
    # class method
    def quak(self):
        print(self.sound)
    def move(self):
        print(self.movement)
    
    # This provides the string representation of the object
    def __str__(self) -> str:
        return f'The {self.sound} and the {self.movement}'


def main():
    donald = Duck()
    donald.move()
    donald.quak()
    print(donald)


if __name__ == '__main__':
    main()