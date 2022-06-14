username = input("Enter your username")
password = input("Enter password")

hidden_password = '*' * len(password)

print(f'{username} password {hidden_password} is {len(password)} letters long')