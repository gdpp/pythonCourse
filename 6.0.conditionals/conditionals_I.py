is_old = False
is_licenced = True

if is_old:
    print('You are old enough to drive')
elif is_licenced:
    print('You can drive now')
else:
    print('You\'re not old enough to drive')

print('End IF')

#Truthy and Falsy

is_truthy = 5
is_falsy = ''

if is_truthy and is_falsy:
    print(True)
else:
    print(False)
    
#ternary operator

a = 5
#condition_if_true if condition else condition_if_false
result = "Valid number" if a else "Invalid Number"
print(result)

is_friend = True
#condition_if_true if condition else condition_if_false
can_message = 'Message Allowed' if is_friend else "Message Blocked"

print(can_message)

#short circuiting
is_dead = True
game_over = True

print(is_dead and game_over)

if is_dead and game_over:
    print("the game is over")

lives = 3
extra_level = False

if lives or extra_level:
    print("The game continues")
    
#logical operators
print( 4 > 5)
print( 4 < 5)
print( 4 == 5)
print('hello' == 'Hello')
print('a' == 'A')
print( 0 != 0)
print(10 != 1)
print(5 <= 6)
print(not(True))





