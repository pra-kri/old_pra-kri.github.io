"""
Creating a stack data-structure in Python.

Stack --> LIFO: Last-in, first-out.

Common uses: 
    - Web-browser back-button (stacks the URLs)
    
    
Functionality of a stack that I need to implement: 
Key: ([_] = todo,  [/] = done)

    [/] - create a new stack, which will contain multiple 'items'. Will use the existing LIST data structure as a base, upon which the stack will be implemented.
    [/] - push --> adds the latest item to the top of the stack
    [/] - pop --> removes the latest item from the top of the stack. Lists already have pop(), so could easily just borrow this.
    [/] - view_top --> looks at the top item from the stack, WITHOUT removing it
    [/] - look at size of stack --> see how many items are in the stack
    [/] - pop_until_empty --> keep popping the stack until its empty. 
    [/] - use a stack to help you reverse a string.
"""



class Stack:
    def __init__(self):
        self.items = []
        # stack will be built on top of Python's list structure.
        # initialises an empty list.

    def stack_push(self, thing):
        self.items.append(thing)

    def view_top(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return ("Stack is empty, you can't really view the top...")

    def stack_pop(self):
        return self.items.pop()

    def view_size(self):
        return len(self.items)

    def pop_until_empty(self):
        while len(self.items) != 0:
            print(self.items.pop())
            #return self.items.pop()
            # return isnt appropriate here, instead have to use print()



#creating an example stack to test the functionality:
stack111 = Stack()
stack111.stack_push(9)
stack111.stack_push(12)
stack111.stack_push(1223232)


"""
#testing lines below:
print("*"*30)
print(stack111.view_size())
print(stack111.view_top())
print(stack111.stack_pop())
print(stack111.view_top())
print(stack111.view_size())
print(stack111.stack_pop())
print(stack111.view_top())
print(stack111.view_size())
print("*"*30)
"""
stack111.pop_until_empty()


# Using a stack to reverse a string:

my_string = "zyxwvutsrqponmlkjihgfedcba"

def string_reversal(str_to_rev):
    # convert string to a normal list:
    list_to_rev = list(str_to_rev)
    temp_stack = Stack()
    reversed_list = []

    for element in list_to_rev:
        temp_stack.stack_push(element)

    while len(temp_stack.items) != 0: #while stack isnt empty...
        reversed_list.append(temp_stack.stack_pop())

    reversed_string = ''.join(reversed_list)

    return(reversed_string)


print(string_reversal(my_string))
