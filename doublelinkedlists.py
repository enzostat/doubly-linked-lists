class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,data):
        """
        Add a node to back of the LL
        Parameters
        """
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove(self, node_value):
        current = self.head

        while current != None:

            if current.data == node_value:
                if self.head == self.tail:
                    self.head = self.tail = None
                    return

                if current.prev != None:
                    current.prev.next = current.next
                    # current.next.prev = current.prev
                else:
                    self.head = self.head.next
                    self.head.prev = None

                if current.next != None:
                    current.next.prev = current.prev
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None

            current = current.next
    
    def show(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next


d = DoublyLinkedList()
d.append(1)
d.append(2)
d.append(3)

d.remove(2)
d.show()
