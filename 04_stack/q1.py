import stack

class Stack(stack.Stack):
    def insert_string(self, value: str):
        for char in value:
            self.push(char)

    def reverse_string(self, value: str):
        self.insert_string(value)
        
        reverse_str = ''
        for _ in range(self.size()):
            reverse_str += self.pop()
        
        return reverse_str

stack = Stack()
value_str = 'We will conquere COVID-19'
reverse_str = stack.reverse_string(value_str)
print('reverse_string("' + value_str + '") should return "' + reverse_str + '"')