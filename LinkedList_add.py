class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLinkedList(self):
        if self.head is None:
            print("Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->",end = " ")
                n = n.ref
            print("None")
            
    def addBegin(self, data):
        newNode = Node(data)
        newNode.ref = self.head
        self.head = newNode

    def addEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref != None:
                n =n.ref
            n.ref = newNode

    def afterNode(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("node not found")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode

    def beforeAdd(self, data, x):
        n = self.head
        while self.head is None:
            print("Empty")
            return
        if self.head.data == x:
            self.addBegin(data)
            return

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print(f"Node with data {x} not found")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode



LL1 = LinkedList()
LL1.addBegin(10)
LL1.addEnd(35)
LL1.addBegin(56)
LL1.afterNode(45, 10)
LL1.beforeAdd(67,10)
LL1.printLinkedList()
