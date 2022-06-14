try:
    with open('test.txt', mode='r') as my_file:
        # text = my_file.write("Hello it's me")
        print(my_file.read())
except FileNotFoundError as err:
    print(err)
except IOError as err:
    print(err)

