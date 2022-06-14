#Generators

def make_list(n):
    result = []
    
    for i in range(n):
        result.append(i * 2)
        
    return result

my_list = make_list(100)

print(my_list)

