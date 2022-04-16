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
    '''
    The Word class represents a word in the form of a string
    attributes: input_word
    methods: populate_stack, popuate_queue, split_string, palindrome_test,
             is_palindrome, is_repeat
    '''

    def __init__(self, input_word):
        '''initialize the word class'''

        # initialize stack and queue
        self.word_stack = Stack()
        self.word_queue = Queue()

        # ensure the input_word variable is a single word string
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

    def split_string(self, queue, number_of_times) -> None:
        '''
        split_string takes in a queue and number variable and splits the
        element in the queue the number of times specified by the user. 
        params:
            self -- the current object
            queue -- the queue object containing a single string
            number_of_times -- int for the number of times to be split
        returns:
            void
        '''

        # cycle through the queue and cut the elements in half the
        # number of times specifid by the input
        for r in range(1, number_of_times + 1):
            for p in range(1, r):
                partial_string = queue.dequeue()
                middle_index = int(len(partial_string) / 2)
                queue.enqueue(partial_string[:middle_index])
                queue.enqueue(partial_string[middle_index:])

    def palindrome_test(self, test_word) -> bool:
        '''
        palindrome_test returns a boolean representing whether the input
        word is a palindrome
        params:
            self -- the current object4
            test_word -- the string being tested as a palindrome
        return:
            bool
        '''

        # create variable to return
        palindrome_flag = True

        # instantiate and populate a stack with the letters of the word
        test_stack = Stack()
        self.populate_stack(test_word, test_stack)

        # instantiate and populate a queue with the letters of the word
        test_queue = Queue()
        self.populate_queue(test_word, test_queue)

        # for each letter in the word test if the next letter from 
        # the stac and queue match.  Set the palindrome_flag to false 
        # if one or more of the letters does not match
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

        # test to ensure number_of_times is of type int
        if not isinstance(number_of_times, int):
            raise ValueError("number_of_times must be of type int")

        # if number_of_times is one, run the palindrome test directly on
        # the input_word
        if number_of_times == 1:

            # test to see if the word is a palindrome
            return self.palindrome_test(self.input_word)

        # if number_of_times is greater than one, split the word up before
        # running the palindrome tests
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
                queue = Queue()

                # add the input word to the queue
                queue.enqueue(self.input_word)

                # split the queue into substrings
                self.split_string(queue, number_of_times)

                # test each of the elements in the queue to ensure it is a 
                # palindrome.  Return False if it is not
                for r in range(number_of_times):
                    if not self.palindrome_test(queue.dequeue()):
                        return False

                return True

        # raise an error if number_of_times is less than 1
        else:
            err = "number_of_times must be greater than or equal to 1"
            raise ValueError(err)

    def is_repeat(self, number_of_times=1) -> bool:
        '''
        is_repeat tests if a string contains the same repeated the
        specified number of times
        params:
            self -- the current object
            number_of_times -- int representing the number of tests
        returns:
            bool
        '''

        # test to ensure the input number is an int
        if not isinstance(number_of_times, int):
            raise ValueError("number_of_times must be of type int")

        # For the purposes of this function, if number_of_times = 1, then
        # the word is considered a reapeat. 
        if number_of_times == 1:
            return True

        # If number_of_times > 1 then run throught the following logic to 
        # test the input string
        elif number_of_times > 1: 

            # create a queue and stack to hold to strings for processing
            queue = Queue()
            previous_word = Stack()

            # add the input word to the queue
            queue.enqueue(self.input_word)
            word_length = int(len(self.input_word) / number_of_times)

            # cycle through the queue and cut the elements in half the
            # number of times specifid by the input
            for r in range(1, number_of_times + 1):
                partial_string = queue.dequeue()

                if len(partial_string) <= word_length:
                    queue.enqueue(partial_string)
                else:
                    queue.enqueue(partial_string[word_length:])
                    queue.enqueue(partial_string[:word_length])

            # test each of the elements in the queue to ensure it is a 
            # repeat of the previous word.  Return False if it is not.
            for r in range(number_of_times):

                # set the element for the first iteration
                if r == 0:
                    previous_word.push(queue.dequeue())

                # compare the previous string and current string.
                # return false if they are not the same word
                else:
                    current_word = queue.dequeue()
                    if previous_word.pop() != current_word:
                        return False 
                    else:
                        previous_word.push(current_word) 

            return True

        # raise an error if number_of_times is less than 1
        else:
            err = "number_of_times must be greater than or equal to 1"
            raise ValueError(err)


if __name__ == "__main__":
    '''Basic tests to run while developing the code'''

    r = Word("racecar")
    print(r.is_palindrome(), "racecar is a palindrome")
    print(r.is_palindrome(), "racecar is a repeated")

    c = Word("Connor")
    print(c.is_palindrome(), "connor is not a palindrome")

    c = Word("racecarracecarracecarracecar")
    print(c.is_palindrome(3), "racecarracecar is a palindrome")
    # print(c.is_repeat(3), "racecarracecar is a repeat")

    c = Word("jmgukndhemmehdnkugmjjmgukndhemmehdnkugmjjmgukndhemmehdnkugmj")
    print(c.is_repeat(3), "jmg is a repeat")
