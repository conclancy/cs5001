''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Quiz 11 - Question 6
clancy.co@northeastern.edu (002781018)
14 April 2022

The file contains a program that allows the user to create a queue ADT
'''

class Queue:
    '''
    The queue class is an ADT that allows users to store and access items 
    in a FIFO manner. 
    '''

    def __init__(self):
        self.data = list()
 
    def enqueue(self, item):
        '''
        the enqueue function adds an item to the queue
        params: a string item
        returns: Void
        '''
        self.data.append(item)

    def  dequeue(self):
        '''
        the dequeue function returns the first item and removes it from the queue
        returns: Void
        '''
        self.data.pop(0)
    
    def dump(self):
        '''
        dump returns the values in the queue 
        returns: a single string for each item in the queue
        '''

        print(self.data)

if __name__ == "__main__":

    # initalize the queue 
    quiz_queue = Queue()

    # Add 5 items to the queue 
    for n in range(5):
        quiz_queue.enqueue(n)
    
    print(quiz_queue.dump())

    # remove 3 items from the queue
    for n in range(3):
        quiz_queue.dequeue()
    
    print(quiz_queue.dump())