"""
# Queue --> FIFO: Fast-in, first-out.

# Common uses: process scheduling, keystrokes, printing queues...etc.

# Functionality of a queue that I need to implement: 
    [/] - create a new queue, which will contain multiple 'items'. Will use the existing LIST data structure as a base, upon which the stack will be implemented.
    [/] - enqueue --> add item to end of queue
    [/] - dequeue --> allows item at front of queue to 'leave'
    [/] - check_size
    [/] - process queue until empty (i.e. dequeue until empty)
    [/] - view_front of queue

"""


class Queue:
    def __init__(self):
        self.items = []
        # similar to my stack implementation, will be built on top of the List struct.

    def enqueue(self, thing):
        self.items.append(thing)

    def dequeue(self):
        return self.items.pop(0)

    def check_size(self):
        return len(self.items)

    def view_front(self):
        if len(self.items) != 0:
            return self.items[0]
        else:
            return ("Queue is empty, you cant view the front of an empty queue...")
            # could just return None instead actually...

    def dequeue_until_empty(self):
        while len(self.items) != 0:
            print(self.items.pop(0))
            


queue111 = Queue()

queue111.enqueue(123123)
queue111.enqueue('AAAAA')
queue111.enqueue('BBB')


"""
# testing lines below:
print(queue111.check_size())
print(queue111.view_front())
print(queue111.dequeue())
print(queue111.dequeue())
print(queue111.check_size())
print(queue111.view_front())
"""
queue111.dequeue_until_empty()
