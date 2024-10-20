class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
        

def LinkedList(self, data):
    def __init__(self, data):
        self.head = None

    
    def printList(self):
        if self.head is None:
            print("Empty")
        else:
            n = self.head
            while n not in None:
                print(n.data,"->",end = " ")
                n = n.ref
            print("none")

LL1 = LinkedList()
LL1.printList()
