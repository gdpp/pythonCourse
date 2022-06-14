from email.generator import DecodedGenerator


def hello(func):
    func()
    
def greet():
    print('Still here')

a = hello(greet)

print(a)

#@decorator
def hello():
    pass

#High Order Functions HOC
def greet(func):
    func()
    
def greet2():
    def func():
        return 5
    return func