def accept_stuffs(*args):
    print(type(args))
    print(args)
    

accept_stuffs(1)
accept_stuffs(1, 3, 5)
accept_stuffs(1, 2, 3, 4, 5)
accept_stuffs()

def my_max(*numbers, nonsense):
    print(nonsense)
    greatest = numbers[0]
    
    for number in numbers:
        if number > greatest:
            greatest = number
    
    return greatest

print(my_max(1, nonsense = "Shazam"))
print(my_max(1, 3, nonsense = "Hooray"))
print(my_max(1, 3, 7, 8, 9, 56, -4, nonsense = "Bonanza"))