with open("cupcakes.txt", "r") as file_object:
    for line in file_object:
        print(line.rstrip())