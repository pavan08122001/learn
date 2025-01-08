class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def deleteAtBeginning(self):
        if self.head is None:
            print("The list is empty")
        self.head = self.head.next
    

    def deleteAtEnd(self):
        if self.head is None:
            print("The List is empty")
            return        
        elif self.head.next is None:
            self.head = None
            return
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None

    def findElement(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f'given value {value} found at position {position}'
            current = current.next
            position += 1
        
        return f'given value {value} not found'



ll = Linkedlist()
ll.insertAtBeginning(1)
ll.insertAtBeginning(2)
ll.insertAtEnd(0)
ll.printList()
print(ll.findElement(1))