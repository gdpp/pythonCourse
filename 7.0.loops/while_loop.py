#while

while True:
    print('infinite')
    break

counter = 5 
while 0 < counter:
    print('minor than')
    counter -= 1
else:
    print('Done with all the work')

while True:
    response = input("Say something: ")
    
    if response == "Bye":
        print("Good Bye")
        break