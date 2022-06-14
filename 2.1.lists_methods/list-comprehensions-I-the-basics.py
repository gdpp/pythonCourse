numbers = [3, 4, 5, 6, 7]
squares = []

#for number in numbers:
#    squares.append(number ** 2)
    
#print(squares)
#print(number)

squares = [number ** 2 for number in numbers]
print(squares)

rivers = ["amazon", "nile", "yangtze"]
print([len(river) for river in rivers])

expressions = ["lol", "rofl", "lmao"]
print([st.upper() for st in expressions])

decimals = [4.95, 3.28, 1.08]
print([int(decimal) for decimal in decimals])