# *args **kwargs

def super_func(*args):
    print(args) #return tuple
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

def hyper_func(**kwargs):
    print(kwargs) #return dict
    
    for key, value in kwargs.items():
        print(f'{key} - {value}')
        
    return None

print(hyper_func(name='gus', age=21, occupation='student'))


def mix_args(*args, **kwargs):
    print(args) #retorna tuple
    print(kwargs) #retorna dict
    
mix_args(1, 2, 3, 4, 5, num=10, x =20, y=200)