# Implementing basic stack and queue data structures
# Note to self: might want to add error handling later...

class Stack:
    def __init__(self, max_size):  # default size should be enough for now
        self.stuff = []  # using a simple list to store items
        self.size_limit = max_size  
    
    # adds new item to stack if there's room
    def push(self, item):
        if len(self.stuff) < self.size_limit:
            self.stuff.append(item)
    
    def pop(self):
        # check if empty first to avoid errors
        if not self.is_empty():
            return self.stuff.pop()
        return None 
    
    def is_empty(self):
        return len(self.stuff) == 0
    
    def __str__(self):
        # quick way to see what's in the stack
        return f"Stack: {self.stuff}"


# Queue implementation - pretty similar to stack
# but different order of operations
class Queue:
    def __init__(self, max_size=100):
        self.data = []  # different name than stack's list
        self.max_size = max_size
    
    # add to front - might be slower but works
    def enqueue(self, item):
        if len(self.data) < self.max_size:
            self.data.insert(0, item)  # insert at beginning
            
    def dequeue(self):
        # remove from end if possible
        if not self.is_empty():
            return self.data.pop()
        return None
    
    # copied from stack because it works the same way
    def is_empty(self):
        return len(self.data) == 0
    
    def __str__(self):
        return f"Queue: {self.data}"  # same format as stack for consistency