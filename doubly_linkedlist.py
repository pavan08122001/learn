class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print(None)

dll=DoublyLinkedlist()
dll.insertAtBeginning(1)
dll.insertAtBeginning(2)
dll.insertAtBeginning(3)
dll.printList()