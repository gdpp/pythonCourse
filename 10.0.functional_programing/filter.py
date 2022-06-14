#filter

my_list = list(range(0, 50))

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)


users = ['gustavo', 'leslie', 'sally', 'nami', 'salem', 'luna', 'daniel']

def search_user(item):
    return item[0] == 'l'

print(list(filter(search_user, users)))
