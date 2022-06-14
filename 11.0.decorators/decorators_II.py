#Decorators

def my_decorator(func):
    def wrap_func(x):
        print('*****')
        func(x)
        print('*****')
    
    return wrap_func

@my_decorator
def hello(greeting):
    print(greeting)
    
hello("Hello")

def bye():
    print('Goodbye')
    
bye()

hello2 = my_decorator(hello)
hello2()

my_decorator(hello)()