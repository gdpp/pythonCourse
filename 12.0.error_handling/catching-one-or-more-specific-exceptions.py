def divide_five_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as error:
        return error
    
    return calculation

print(divide_five_by_number(0))
print(divide_five_by_number(10))
print(divide_five_by_number("none"))