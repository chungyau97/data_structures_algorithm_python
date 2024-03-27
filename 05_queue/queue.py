from collections import deque

class Queue:
    def __init__(self) -> None:
        self.container = deque()
    
    def enqueue(self, value):
        self.container.appendleft(value)
    
    def dequeue(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return self.size() == 0
    
# queue = Queue()
# queue.enqueue('first thing')
# queue.enqueue('second thing')
# print(queue.dequeue())
# print(queue.is_empty())