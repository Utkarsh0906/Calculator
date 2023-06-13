from os import system
def addition(a,b):
    """Take two numbers and add the second number to the first number."""
    return a+b
def subtraction(a,b):
    """Take two numbers and sbutract the second number from the first number"""
    return a-b
def multiplication(a,b):
    """Take two numbers and multiply the second number to the first number"""
    return a*b
def division(a,b):
    """Take two numbers and divide the first number by the second number"""
    return a/b
def modulus(a,b):
    """Take two numbers and find the remainder after dividing the first number by the second number"""
    return a%b
def calculator():
    system('cls')
    print("Welcome! Do your calculations here!!")
    a = float(input("Enter First Number: "))
    o = input("Enter The Operation: ")
    b = float(input("Enter Second Number: "))
    while(True):
        operators = {'+': addition,
                    "-": subtraction,
                    "*": multiplication,
                    "/": division,
                    "%": modulus}
        result = operators[o](a,b)
        print(f"{a} {o} {b} = {result}")
        call = input("Press 'Y' to continue calculation with this result and 'N' for stop: ").lower()
        if(call == "n"):
            break
        a = result
        o = input("Enter Next Operation: ")
        b = float(input("Enter Next Number: "))
    call = input("Do you want to conitnue using the calculator. Enter 'Y' for Yes and 'N' for No: ").lower()
    if(call == 'y'):
        calculator()
calculator()