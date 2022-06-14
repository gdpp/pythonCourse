the_simpson = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']

for character in the_simpson[::-1]:
    print(f"{character} has a total of {len(character)}")
    
print(reversed(the_simpson))
print(type(reversed(the_simpson)))

for character in reversed(the_simpson):
    print(f"{character} has a total of {len(character)}")