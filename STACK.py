import queue
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self,data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top # type: ignore
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top= self.top.next
            popped_node.next = None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


#using Lifoqueue 

stack_using_queue = queue.LifoQueue(maxsize=0)

stack_using_queue.put("Teja")
stack_using_queue.put("this is")
stack_using_queue.put("hello")

print(stack_using_queue.get())
print(stack_using_queue.get())
print(stack_using_queue.get())