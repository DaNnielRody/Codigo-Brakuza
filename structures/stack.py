# Last In First Out

# Pilha:
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def __len__(self):
        return len(self.stack)

stack = Stack()

stack.push(12)
stack.push(24)
stack.push(32)
stack.push(47)

while not stack.is_empty():
    print(f"Última a entrar: {stack.peek()}")
    print(f"Tamanho: {len(stack)}")
    stack.pop()
    print("*************")
    
# É assim que o seu CTRL + Z é feito! 