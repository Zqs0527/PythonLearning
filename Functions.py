def main():
    inputs = dict(x="ttt",y="ssss")
    example_keywords_arguments(**inputs)
    x = ("rule", "yellow")
    example(*x)
    kitten()

def kitten():
    print('Meow.')

# asterisk args: arguments list
def example(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print("blabla")
# double asterisk kwargs: dictionary
def example_keywords_arguments(**kwargs):
    if len(kwargs):
        for k in kwargs:
           print(f'The key is {k} and the value is {kwargs[k]}')
    else:
        print("blabla")

def f1():
    def f2():
        print('this is f2')
    return f2


if __name__ == '__main__':
    x = f1()
    x()
