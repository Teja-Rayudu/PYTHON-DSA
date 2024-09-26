class Node:
    def __init__(self,data):
        self.head = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.count = 0

    def insert_at_beginning(self,data):
        new = Node(data)
        if self.head is not None:
            new.next = self.head  # type: ignore
            self.head = new
        else:
            self.tail=new
            self.head = new
        self.count+=1
    
    def insert(self,data):
        self.insert_at_beginning(data)

    def insert_at_end(self,data):
        new = Node(data)
        if self.head is not None:
            self.tail.next = new # type: ignore
            self.tail = new
        else:
            self.head = new
            self.tail = new
        self.count+=1
    
    def remove_at_end(self):
        curr = self.head
        while curr.next.next is not None: # type: ignore
            curr = curr.next # type: ignore
        curr.next = None #type: ignore
        self.count-=1
    
    def printList(self):
        current = self.head
        while current is not None:
            print(current.head)
            current = current.next

    def search(self,data):
        current = self.head
        while current is not None:
            if current.head ==data:
                return True
            else:
                current = current.next
        return False
    
    def search_at_index(self,data):
     try:
        if self.head is not None:
            curr = self.head
            for i in range(data):
                curr = curr.next #type: ignore
            print(curr.head) # type: ignore
        else:
            print("List is Empty")
     except:
         print("{some} is not in range".format(some=data))

    def remove_at_beggining(self):
        curr = self.head
        self.head = self.head.next #type: ignore
        curr.next=None  # type: ignore
        self.count-=1
    
    def reverse_LinkedList(self):
        if self.head is not None:
            prev = None
            current = self.head
            while current is not None:
                next_node = current.next
                current.next = prev # type: ignore
                prev = current
                current = next_node
        else:
            print("List is empty")
        self.head = prev
    
    def Size(self):
        return self.count


