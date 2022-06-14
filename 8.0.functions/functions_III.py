def sum(a, b):
    return a + b

print(sum(3, 4))
print(sum(10, 4))
print(sum(32, 4))

total = sum(5, 5)

print(total)

print(sum(5, total))

def first_func(num1, num2):
    def second_func(n1, n2):
        return n1 + n2
    
    return second_func(num1, num2)
    

result = first_func(10, 20)

print(result)


def test(a):
    '''
    INFO: This functions tests and prints param a
    '''
    print(a)

test('a')

help(test)

print(test.__doc__)