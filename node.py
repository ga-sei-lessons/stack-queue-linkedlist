class Node:
    '''
        A singlely linked list node
    '''
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'