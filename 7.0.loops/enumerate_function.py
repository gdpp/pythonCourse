for x, char in enumerate('hello'):
    print(x, char)
    
for x, num in enumerate([1, 2, 3]):
    print(x, num)
    
for i, tup in enumerate(('a', 'b', 'c')):
    print(i, tup)
    
for a, b in enumerate(list(range(100))):
    if b == 50:
        print(f'the index of 50 is: {a}')