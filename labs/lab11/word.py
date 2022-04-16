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
            if ' ' not in input_word:
                self.input_word = input_word.lower()
            else:
                err = 'input word must be a single word string without spaces'
                raise ValueError(err)
        else: 
            raise ValueError('input_word must be of type string')

        # populate the stack and the queue
        self.populate_stack(self.input_word, self.word_stack)
        self.populate_queue(self.input_word, self.word_queue)

    def populate_stack(self, word, stack) -> None:
        '''
        create stack is an internal function used to populate the word stack
        params:
            self -- the current object
            word -- the word to be added to the stack
            stack -- the stack to be populated
        returns:
            void
        '''

        # ensure we are working with a clean stack
        stack.clear()

        # add every letter in the word as an element in the stack
        for i in word:
            stack.push(i)

    def populate_queue(self, word, queue) -> None:
        '''
        create queue is an internal function used to populate the word queue
        params:
            self -- the current object
        returns:
            void
        '''

        # ensure we are working with a clean queue
        self.word_queue.clear()

        # add every letter in the word as an element in the queue
        for i in word:
            queue.enqueue(i)

    def palindrome_test(self, test_word) -> bool:
        # create variable to return
        palindrome_flag = True

        test_stack = Stack()
        self.populate_stack(test_word, test_stack)

        test_queue = Queue()
        self.populate_queue(test_word, test_queue)

        for letter in test_word:
            if test_stack.pop() != test_queue.dequeue():
                palindrome_flag = False

        return palindrome_flag

    def is_palindrome(self, number_of_times=1) -> bool:
        '''
        tests the word to see if it is a palindrome or a nested palindrome
        matching the number of times entered into the function
        params:
            self -- the current object
            number_of_times -- the number of times the palindrome is nested
        returns:
            bool
        '''

        if not isinstance(number_of_times, int):
            raise ValueError("number_of_times must be of type int")

        if number_of_times == 1:

            # test to see if the word is a palindrome
            return self.palindrome_test(self.input_word)

        elif number_of_times > 1: 

            # all nested palindromes will have an even number of elements. 
            # odd + odd = even 
            # even + even = even 
            # only odd + even = odd, meaning the two portions are not the same
            # and are not palindormes
            if len(self.input_word) % 2 != 0:
                return False
            else:
                # create a queue to hold to strings for processing
                q = Queue()

                # add the input word to the queue
                q.enqueue(self.input_word)

                # cycle through the queue and cut the elements in half the
                # number of times specifid by the input
                for r in range(1, number_of_times + 1):
                    for p in range(1, r):
                        partial_string = q.dequeue()
                        middle_index = int(len(partial_string) / 2)
                        q.enqueue(partial_string[:middle_index])
                        q.enqueue(partial_string[middle_index:])

                # test each of the elements in the queue to ensure it is a 
                # palindrome.  Return False if it is not
                for r in range(number_of_times):
                    if not self.palindrome_test(q.dequeue()):
                        return False

                return True

        else:
            err = "number_of_times must be greater than or equal to 1"
            raise ValueError(err)


if __name__ == "__main__":
    r = Word("racecar")
    print(r.is_palindrome(), "racecar is a palindrome")

    c = Word("Connor")
    print(c.is_palindrome(), "connor is not a palindrome")

    c = Word("racecarracecarracecarracecar")
    print(c.is_palindrome(3), "racecarracecar is a palindrome")
