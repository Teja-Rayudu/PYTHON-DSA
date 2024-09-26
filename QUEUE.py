import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node #type: ignore
            self.tail = new_node
    
    def dequeue(self):
        if self.head is not None:
            current_node = self.head
            self.head=self.head.next
            current_node.next=None
            
            if self.head == None:
                self.tail =None
        
    
    def printQueue(self):
            current = self.head
            while current is not None:
                print(current.data) # type: ignore
                current = current.next # type: ignore

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.printQueue()

q.dequeue()

print()
q.printQueue()

# USING QUEUE MODULE:
Q = queue.Queue()

Q.put("Hi")
Q.put("this")
Q.put("is")
Q.put("Teja Rayudu")

