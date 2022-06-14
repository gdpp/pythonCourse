def length(word):
    return len(word)

print(length("gustavo"))
print(length(word = "gustavo"))


def collect_keyword_args(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(f"The key { key } and the value is { value}")
    
collect_keyword_args(a = 2, b = 3, c =4, d = 5)


def args_and_kwargs(a, b, *args, **kwargs):
    print(f"The total of your regular arguments a and b is { a + b }")
    print(f"The total of your args tuple is { sum(args) }")
    
    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    
    print(f"The total of your kwargs dictionary is { dict_total }")

args_and_kwargs(1, 2, 3, 4, 5, 6, x = 8, y = 9, z = 10)