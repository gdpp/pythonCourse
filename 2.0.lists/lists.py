li = ['Hello', "user"]
li2 = ['a', 'b', 'c']
li3 = ['a', 1, True]

amazon_cart = ['notebooks', 'applewatch', 'toys', 'grapes']


print(amazon_cart[0])

amazon_cart[0] = 'laptop'

print(amazon_cart[0::2])

#Matrix
matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(matrix[0][1])

#List methods
abilities = ['punch', 'kick', 'kick', 'jump', 'throw']
print(len(abilities))

#add
abilities.append('climb')
abilities.insert(5, 'fire punch')
print(abilities)
new_abilities = abilities.extend(['frozen kick'])
print(abilities)

#remove
abilities.pop()
print(abilities)

abilities.pop(0)
print(abilities)

abilities.remove('jump')
print(abilities)

print(abilities.index('kick', 0, 4))

print('kick' in abilities)

print(abilities.count('kick'))
#abilities.clear()
#print(abilities)

basket = ['a', 'x', 'c', 'y', 'e', 'f']

sorted(basket) #produce una nueva lista

basket.sort()
basket.reverse()
print(basket)

#useful tricks in lists
ex_list = [1, 5, 3, 9, 2, 6, 10, 8, 4, 7]

print(list(range(51)))
print(list(range(1, 100)))

sentence = ' '
new_sentence = sentence.join(['joined', 'with', 'join', 'method'])

print(new_sentence)

#list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)