class Stack():

    def __init__(self, capacity, list_stack=[]):
        self.capacity = capacity
        self.list_stack = list_stack

    def is_empty(self):
        if not self.list_stack:
            return f"Stack is empty"
        return f"Stack is not empty"

    def is_full(self):
        if len(self.list_stack) == self.capacity:
            return f"Stack is full"
        return f"Stack is not full"

    def pop(self):
        if not self.list_stack:
            return f"Stack is empty"
        else:
            pop_value = self.list_stack.pop(-1)
        return pop_value

    def push(self, added_num):
        if self.capacity > len(self.list_stack):
            self.list_stack.append(added_num)
            return self.list_stack
        else:
            return f"Stack is full"

    def top(self):
        if not self.list_stack:
            return f"Stack is empty"
        top_value = self.list_stack[-1]
        return top_value


stack_1 = Stack(capacity=5)
stack_1.push(1)
stack_1.push(2)

print(stack_1.is_full())
print(stack_1.top())
print(stack_1.pop())
print(stack_1.top())
print(stack_1.pop())
print(stack_1.is_empty())
