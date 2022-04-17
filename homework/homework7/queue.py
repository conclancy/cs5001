''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 11 - Homework 7
clancy.co@northeastern.edu (002781018)
17 APR 22 

The file contains the queue class that can be used to make a queue object
from a python list.  The class includes enqueue and dequeue cabilities. 
'''

class Queue:

    def __init__(self):
        '''constructor for the queue class'''

        # initialize a list that will hold the items in the queue
        self.data = list()

    def enqueue(self, item) -> None:
        '''
        enqueue allows you to add an item to the end of the queue
        params:
            self -- the current object
            item -- the item to be added to the end of the queue
        return: 
            void
        '''

        # add the item to the queue
        self.data.append(item)

    def dequeue(self) -> object:
        '''
        dequeue allows you to remove an item from the front of the queue
        params:
            self -- the current object
        return:
            void
        '''

        # remove and return the first item to the queue
        return self.data.pop(0)

    def dump(self) -> None:
        '''
        dump is a debugging method that prints the queue in FIFO order
        params:
            self -- the current object
        returns:
            void
        '''

        # print the data list for debugging
        print(self.data)
    
    def clear(self) -> None:
        '''
        clear removes all items from the queue
        params:
            self -- the current object
        returns:
            void
        '''
        self.data = list()
        

if __name__ == "__main__":
    test_stack = Queue()

    test_stack.enqueue(1)
    test_stack.enqueue(2)
    test_stack.enqueue(3)
    test_stack.enqueue("test")

    test_stack.dump()

    test_stack.dequeue()
    test_stack.dump()

    test_stack.dequeue()
    test_stack.dump()

    test_stack.dequeue()
    test_stack.dump()

    test_stack.dequeue()
    test_stack.dump()

    test_stack.enqueue(1)
    test_stack.enqueue(2)
    test_stack.enqueue(3)
    test_stack.enqueue("test")

    test_stack.dump()

    test_stack.clear()

    test_stack.dump()
