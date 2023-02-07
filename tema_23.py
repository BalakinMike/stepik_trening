def repeater(func):
    def inner(*args):
        func(*args)
        func(*args)
    return



@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7)