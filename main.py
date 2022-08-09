'''
this 
multiple
line
'''


def isNum(num):
    return type(num) == int or type(num) == float

# this function takes 1 argument which is a list of numbers and adds them
def add(a):
    result = 0
    for num in a:
        if isNum(num):
            result += num
        else:
            raise Exception("Error: not a number")
    return result

# this function takes 1 argument which is a list of numbers and subtracts them
def subtract(a):
    count = 0
    result = 0
    for num in a:
        # first time in the loop
        if count == 0:
            result = num
            count += 1
            continue
        if isNum(num):
            result -= num
        else:
            raise Exception("Error: not a number")
        count += 1
    return result

# main part of the program
try:
    myList = map(float, input("Enter a list of numbers to add/subtract: ").split())
    choice = int(input("Enter 1 to add, 2 to subtract: "))
    if choice == 1:
        print(add(myList))
    elif choice == 2:
        print(subtract(myList))
    else:
        print("How did I get here")
except:
    print("An error occurred")