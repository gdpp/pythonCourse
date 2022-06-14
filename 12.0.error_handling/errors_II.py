#Error Handling

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please enter numbers {err}')

print(sum(3, 4))
print(sum(3, '4'))