class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''Adds a node to the back of the LL
        Parameters:
            data - any value
        '''
        new_node = Node(data)
        if self.head == None: # edge case for inserting into an empty LL
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail # add to the end of the tail
            self.tail.next = new_node # add forward relationship to the old tail
            self.tail = new_node # set new tail

    def sortedInsert(self, data):
        '''Insert a new node to LL in the correct sorted position'''

        # current = self.head
        new_node = Node(data)
        #edge case #1: inserting into an empty LL
        if self.head == None:
            self.append(data)
            return
        
        # edge case number 2: inserting at the head
        if self.head.data >= new_node.data:
            new_node.next = self.head
            # self.head.prev = new_node
            # self.head = new_node
            self.head = self.head.prev = new_node
        else:
            current = self.head
            #traverse the linked list and find the node before the spot we want to insert @
            while current.next != None and current.next.data < data:
                current = current.next
            
            new_node.next = current.next #set new node's relationship to the next node
            if current.next == None:
                self.tail = new_node
            if current.next != None:
                new_node.next.prev = new_node
            
            current.next = new_node
            new_node.prev = current

                

    def remove(self, node_value):
        current = self.head

        while current != None: # Traverse the linked list
            if current.data == node_value: # We found the item to delete
                if self.head == self.tail: # Edge case 1 - Removing Head AND Tail ie) LL is of size 1
                    self.head = self.tail = None
                    return
                
                if current.prev != None: 
                    current.prev.next = current.next # Set the prev node's next ptr 
                else: # Edge case 2 - Removing the Head
                    self.head = self.head.next
                    self.head.prev = None
                
                if current.next != None:
                    current.next.prev = current.prev # Set the next node's prev ptr
                else: # Edge case 3 - Removing the tail
                    self.tail = self.tail.prev
                    self.tail.next = None

            current = current.next # traverse

    def show(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

d = DoublyLinkedList()
# d.append(1)
d.sortedInsert(3)
d.sortedInsert(9)
d.sortedInsert(2)
d.sortedInsert(4)

d.show()