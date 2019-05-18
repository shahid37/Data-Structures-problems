from stack import Element
from stack import Stack

my_stack = Stack()
my_stack.push(5)
my_stack.push(6)
my_stack.push('Shahid')
my_stack.push(8)
my_stack.print()
print()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print()
print(my_stack.top.value)
