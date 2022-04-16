''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 11 - Word
clancy.co@northeastern.edu (002781018)
16 APR 22 

The file contains the word class that can be used to determine if a word 
meets the definition of a palindrome using stacks and queues.
'''

from queue import Queue
from stack import Stack

class Word:

    def __init__(self, input_word):
        '''initialize the word class'''

        # initialize stack and queue
        self.word_stack = Stack()
        self.word_queue = Queue()

        if isinstance(input_word, str):
            self.input_word = input_word
        else: 
            raise TypeError('input_word must be of type string')

        # populate the stack and the queue
        self.populate_stack()
        self.populate_queue()
    
    def populate_stack(self) -> None:
        '''
        create stack is an internal function used to populate the word stack
        params:
            self -- the current object
        returns:
            void
        '''

        # add every letter in the word as an element in the stack
        for i in self.input_word:
            self.word_stack.push(i)
        
        self.word_stack.dump()

    def populate_queue(self) -> None:
        '''
        create queue is an internal function used to populate the word queue
        params:
            self -- the current object
        returns:
            void
        '''

        # add every letter in the word as an element in the queue
        for i in self.input_word:
            self.word_queue.enqueue(i)
        
        self.word_queue.dump()


if __name__ == "__main__":
    Word("racecar")
        