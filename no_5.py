# Implement a simple calculator using functions.
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if a == 0 or b == 0:
        return ZeroDivisionError
    else:
        return a / b

def calculator():
    a = int(input("Enter 1st Number - "))
    b = int(input("Enter 2nd number - "))

    ch = int(input("Enter choice 1. ADD  2. SUBTRACT 3. MULTIPLY 4. DIVISION\n"))
    operations = {
        1: add,
        2: sub,
        3: mul,
        4: div
    }

    if ch in operations:
        result = operations[ch](a,b)
        print(result)
    else:
        print("Invalid ")

calculator()
