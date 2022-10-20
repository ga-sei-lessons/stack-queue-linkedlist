# from < where to import > import < what >
from node import Node

class Stack:
    '''
        a Stack implemented with a singly linked list
    '''
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, data):
        '''
            adds item to stack
        '''
        # create a new node
        # set the new node's next value to be whatever is in the head
        new_node = Node(data, self.head)
        # overwrite the head with the new node
        self.head = new_node
        self.size += 1

    def pop(self):
        '''
            removes item from stack -- returns the popped item
        '''
        # if the list is empty -- return None
        if self.head == None:
            return None
        
        # otherwise, permit the popping operation
        # store a reference to the current head
        popped_head = self.head
        # overwrite the current head with the next of the current head
        self.head = self.head.next
        # decrement size 
        self.size -= 1
        # return our stored node we popped off
        return popped_head
            

    def peek(self):
        '''
            returns the first item in the stack without removing it
        '''
        return self.head

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(f'head: {my_stack.peek()}, head\'s next: {my_stack.peek().next}')
print(f'popping 3: {my_stack.pop()}')
print(f'head: {my_stack.peek()}, head\'s next: {my_stack.peek().next}')
print(f'popping 2: {my_stack.pop()}')
print(f'head: {my_stack.peek()}, head\'s next: {my_stack.peek().next}')
print(f'popping 1: {my_stack.pop()}')
print(f'head: {my_stack.peek()}')
print(my_stack.pop())