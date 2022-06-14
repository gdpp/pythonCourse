# def reverse(st):
#     start_index = 0
#     last_index = len(st) - 1 #4
#     reversed_string = ""
    
#     while last_index >= start_index:
#         reversed_string = reversed_string + st[last_index]
#         last_index -= 1
    
#     return reversed_string

def reverse(st):
    if len(st) <= 1:
        return st
    
    return st[-1] + reverse(st[0:-1])

print(reverse("straw"))