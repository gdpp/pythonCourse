# def count_down_from(number):
#     start = number
    
#     while start > 0:
#         print(start)
#         start -= 1

def count_down_from(num):
    if num <= 0:
        return
    
    print(num)
    count_down_from(num - 1)

count_down_from(5)