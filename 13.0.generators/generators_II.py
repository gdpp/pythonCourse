#Generators

from operator import ne


def generator_function(num):
    for i in range(num):
        yield i * 2
        
g = generator_function(50)

next(g)
next(g)
next(g)

print(next(g))
 