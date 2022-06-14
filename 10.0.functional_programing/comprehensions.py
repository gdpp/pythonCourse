#list comprehension

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
my_list3 = [num ** 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

#set comprehension
 
my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0, 100)}
my_set3 = {num ** 2 for num in range(0, 100)}
my_set4 = {num ** 2 for num in range(0, 100) if num % 2 == 0}

print(my_set)
print(my_set2)
print(my_set3)
print(my_set4)

#dictionary comprehension

simple_dict = {
    'a': 1, 
    'b': 2
}

my_dict = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)