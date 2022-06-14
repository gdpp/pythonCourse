#parameters
def say_hello(name, emoji):
    print(f'Hello {name} {emoji}')

#default parameters
def say_goodbye(name, emoji=':D'):
    print(f'Hello {name} {emoji}')

#positional arguments
say_hello('Gustavo', ':)')
say_hello('Leslie', ':*')

#keyword argumnets
say_hello(emoji=':D', name='Leslie')
say_hello(emoji='D:', name='Daniel')

say_goodbye("Timmy")
say_goodbye("Naruto")