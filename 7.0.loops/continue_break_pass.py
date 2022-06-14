my_list = [1, 2, 3]
i = 0

for _ in my_list:
    print(_)
    break

while i < len(my_list):
    print(my_list[i])
    i += 1
    break

for _ in my_list:
    continue
    print(_)
    #not print

while i < len(my_list):
    i += 1
    continue
    print(my_list[i])
    #not print

for _ in my_list:
    pass

while i < len(my_list):
    pass