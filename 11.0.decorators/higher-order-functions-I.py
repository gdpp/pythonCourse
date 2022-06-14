def one():
    return 1

print(type(one))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(func, a, b):
    return func(a, b)
    
print(calculate(add, 6, 11))
print(calculate(subtract, 245, 234))