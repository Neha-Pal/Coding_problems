queue = []

def enqueue():
    e = int(input("Enter element - "))
    queue.append(e)
    print(queue)

def dequeue():
    if not queue:
        print("Empty queue")
    else:
        queue.pop(0)
        print(queue)

while True:
    choice = int(input("Enter your choice - 1.ENQUEUE 2.DEQUEUE 3.Exit \n"))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    else:
        print("Exit..")
