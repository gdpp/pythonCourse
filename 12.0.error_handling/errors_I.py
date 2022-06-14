#Error Handling
while True:
    try:
        age = int(input('What\'s your age? '))
        10 / age
        raise Exception('hey cut it out')
    # except ValueError:
    #     print('Please enter a number')
    #     continue
    except ZeroDivisionError:
        print('Please enter age higher than zero')
        break
    else:
        print('Good bye')
        break
    finally:
        print('End program')