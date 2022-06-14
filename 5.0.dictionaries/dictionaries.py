#Dictionaries
dictionary = {
    'a': [1, 2, 3],
    'b': "hello",
    'x': True
}

print(dictionary['a'])
print(dictionary['a'][1])
print(dictionary['a'][2])
print(dictionary['b'])
print(dictionary['x'])

my_dict_list = [
    {
        'a': [1, 2, 3],
        'b': "hello",
        'x': True,
        'z': 'Hi'
    },
    {
        'a': [4, 5, 6],
        'b': "goodbye",
        'x': False,
        'z': 'Bye'
    }
]

print(my_dict_list)

print(my_dict_list[0].get('z', 100))

user = dict(name='timmy', age=20)
print(user)

print('name' in user.keys())
print('timmy' in user.values())
print(user.items())

user2 = user.copy()

age = user.pop('age')

print(age)

print(user.update({'age': 100}))

print(user)

user.clear()

print(user)
print(user2)