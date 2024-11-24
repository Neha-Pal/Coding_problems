import queue

queue = queue.PriorityQueue()
elements = []
def enqueue():
    priority = int(input("Enter Priority - "))
    element = input("Enter element - ")
    queue.put((priority, element))
    print(f"Element - {element}: priority - {priority}")
    elements.append((element,priority))
    print(elements)

def dequeue():
    if not queue:
        print("empty")
    else:
        priority, element = queue.get()
        print(f"Dequeued - {element} with priority - {priority}")
        elements.remove((element, priority))

while True:
    choice = int(input("Enter choice - 1.Add 2.Delete 3.Exit\n"))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    else:
        print("Exit..")
