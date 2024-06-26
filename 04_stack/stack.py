from collections import deque

class Stack:
    def __init__(self) -> None:
        self.container = deque()

    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def is_empty(self):
        return self.size() == 0
    
# stack = Stack()
# stack.push('first thing')
# stack.push('second thing')
# print(stack.peek())
# stack.pop()
# print(stack.size())
# print(stack.is_empty())
# print(stack.container)