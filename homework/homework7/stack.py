''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 11 - Word
clancy.co@northeastern.edu (002781018)
16 APR 22 

The file contains the stack class that can be used to make a stack object
from a python list.  The class includes push and pop cabilities. 
'''

class Stack:

    def __init__(self):
        '''constructor for the stack class'''

        # initialize a list that will hold the items in the stack
        self.data = list()
    
    def push(self, item) -> None:
        '''
        push allows you to add an item to the top of the stack
        params:
            self -- the current object
            item -- the item to be added to the top of the stack
        return: 
            void
        '''

        # add the item to the stack
        self.data.append(item)

    def pop(self) -> object: 
        '''
        pop allows you to remove an item from the top of the stack
        params:
            self -- the current object
        returns: 
            void
        '''

        # remove and return the item from the top of the stack
        return self.data.pop()

    def dump(self) -> None:
        '''
        dump is a debugging method that prints the stack in LIFO order
        params:
            self -- the current object
        returns:
            void
        '''

        # print each item starting with the last items first
        for e in range(len(self.data) -1, -1, -1):
            print(self.data[e])

    def clear(self) -> None:
        '''
        clear removes all items from the stack
        params:
            self -- the current object
        returns:
            void
        '''
        self.data = list()

if __name__ == "__main__":
    test_stack = Stack()

    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push("test")

    test_stack.dump()

    test_stack.pop()
    test_stack.dump()

    test_stack.pop()
    test_stack.dump()

    test_stack.pop()
    test_stack.dump()

    test_stack.pop()
    test_stack.dump()

    test_stack.push(1)
    test_stack.push(2)
    test_stack.push(3)
    test_stack.push("test")

    test_stack.dump()

    test_stack.clear

    print("current stack:", test_stack.dump())

