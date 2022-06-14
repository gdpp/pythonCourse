#Functions
#DRY
def say_hello():
    print("HELLOOOOO!")
    
say_hello()


image = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

def show_tree():
    for row in image:    
        for x in row:
            if x == 1:
                print('4', end='')
            else:
                print(' ', end='')
            
        print('')

show_tree()
show_tree()
show_tree()
show_tree()