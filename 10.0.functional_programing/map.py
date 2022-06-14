#map

my_list = [1, 2, 3]

def multiply_by5(item):    
    return item * 5

print(list(map(multiply_by5, my_list)))


def multiply_words(item):
    return item * 2

print(list(map(multiply_words, 'Hello')))


my_other_list = [10, 20 , 30]

def pow_by5(item):
    return item ** 5

print(list(map(pow_by5, my_other_list)))