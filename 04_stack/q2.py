from stack import Stack

parenthesis_dict = {']':'[', '}':'{', ')':'('}

def is_parantheses_balance(equation: str):
    stack = Stack()

    for char in equation:
        if char == '{' or char == '[' or char == '(':
            stack.push(char)
            continue

        elif char == '}' or char == ']' or char == ')':
            if stack.is_empty() == True:
                return False
            elif(parenthesis_dict[char] != stack.pop()):
                return False
            
    return True

print(is_parantheses_balance('({a+b})'))
print(is_parantheses_balance('))((a+b}{'))
print(is_parantheses_balance('((a+b))'))
print(is_parantheses_balance('))'))
print(is_parantheses_balance('[a+b]*(x+2y)*{gg+kk}'))