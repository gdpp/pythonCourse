def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number == 0:
        return "Neither, It's zero!"
    else:
        return "Negative!"
    
print(positive_or_negative(1))
print(positive_or_negative(10))
print(positive_or_negative(1456))
print(positive_or_negative(-3451))
print(positive_or_negative(-235))
print(positive_or_negative(-3))
print(positive_or_negative(0))