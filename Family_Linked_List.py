class Node:
    def _init_(self,name,age):
        self.name = name
        self.age = age
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def _init_(self):
        self.head = None
        self.tail = None

    def addNode(self, name,age):
        # Create a new node
        newNode = Node(name,age)

        if (self.head == None):
            # Both head and tail will point to newNode
            self.head = self.tail = newNode
            # head's previous will point to None
            self.head.previous = None
            # tail's next will point to None, as it is the last node of the list
            self.tail.next = None
        else:
            # newNode will be added after tail such that tail's next will point to newNode
            self.tail.next = newNode
            # newNode's previous will point to tail
            newNode.previous = self.tail
            # newNode will become new tail
            self.tail = newNode
            # As it is last node, tail's next will point to None
            self.tail.next = None

    def display(self):
        # Node current will point to head
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while (current != None):
            # Prints each node by incrementing pointer.
            print(current.name)
            
            current = current.next

dList = DoublyLinkedList()
#Add nodes to the list
dList.addNode("N",18)
dList.display()