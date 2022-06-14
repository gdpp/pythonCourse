powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    power = []
    
    for n in numbers:
        power.append(n ** 2)
    
    return power

print(squares(powerball_numbers))


def convert_to_float(numbers):
    float_numbers = []
    
    for n in numbers:
        float_numbers.append(float(n))
        
    return float_numbers

print(convert_to_float(powerball_numbers))


def even_or_odd(numbers):
    resp = []
    
    for n in numbers:
        if n % 2 == 0:
            resp.append(True)
        else:
            resp.append(False)
    
    return resp 

print(even_or_odd(powerball_numbers))