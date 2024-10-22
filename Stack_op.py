# PUSH POP in one code

stack = []
def push():
    e = int(input("Enter a number:"))
    stack.append(e)
    print(stack)

def pop():
    if not stack:
        print("Empty stack")
    else:
        stack.pop()
        print(stack)

while True:
    choice = int(input("Enter choice - 1.PUSH  2.POP  3.Exit\n"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print("exit..")
        break




