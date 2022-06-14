from random import randint
import sys

first_value = int(sys.argv[1])
end_value = int(sys.argv[2])
response = randint(first_value, end_value)

while True:
    try:
        guess = int(input(f"Guess a number between {first_value} to {end_value}: "))
        if  first_value < guess < end_value:
            if guess == response:
                print("Congratulations!!!, you Win")
                break
        else:
            print(f'Enter a number between {first_value} and {end_value}')
    except ValueError:
        print('Please enter a number')
        continue