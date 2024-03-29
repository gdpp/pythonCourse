def add_positive_numbers(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or Both of the values are invalid")
        
        return a + b
    except ValueError as e:
        return f"Error, {e}"
    
print(add_positive_numbers(10, 5))
print(add_positive_numbers(-2, 3))
print(add_positive_numbers(2, -9))