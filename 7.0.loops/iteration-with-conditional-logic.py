values = [3, 6, 9, 12, 15, 18, 21, 24]
other_values = [5, 10, 15, 20, 25, 30]

def odd_sum(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 1:
            total += n
    
    return total

# print(odd_sum(values))
# print(odd_sum(other_values))


def greatest_number(numbers):
    major = numbers[0]
    for n in numbers:
        if n > major:
            major = n
    
    return major

print(greatest_number([1, 2, 3]))
print(greatest_number([3, 2, 1]))
print(greatest_number([4, 5, 5]))
print(greatest_number([-3, -2, -1]))