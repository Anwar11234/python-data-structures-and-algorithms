class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self , item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)      

q = Queue()
q.enqueue(1)                  
q.enqueue(2)                  
q.enqueue(3)
# 1 2 3 
q.dequeue() # 2 3
print(q.items)                  