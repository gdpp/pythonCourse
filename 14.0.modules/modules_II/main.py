from collections import Counter, defaultdict

li = [1, 2, 3, 4, 5, 6, 7, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5]
print(Counter(li))

sentence = 'blah blah blah thinking about python'

print(Counter(sentence))

dictionary = defaultdict(lambda: 'does not exist', {'a': 1, 'b': 2})

print(dictionary['a'])
print(dictionary['c'])