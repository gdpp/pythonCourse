#Sets
from hashlib import new


my_list = [1, 2, 3, 4, 5]

my_set = set(my_list)

my_set.add(100)
my_set.add(2)

print(my_set)

print(1 in my_set)

print(len(my_set))

new_set = my_set.copy()
my_set.clear()

print(new_set)
print(my_set)