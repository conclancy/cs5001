''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 11 - Word
clancy.co@northeastern.edu (002781018)
16 APR 22 

The file contains the tests for the Word class.
'''

from queue import Queue
from stack import Stack
from word import Word
import unittest

class WordTest(unittest.TestCase):
    '''
    WordTest extends the TestCase class to test the functionality
    of the Word Class
    '''

    def test_init(self):
        '''Test the initalization of a word'''

        # basic test to ensure functionality 
        word = Word("racecar")
        self.assertEqual(word.input_word, "racecar")

        # ensure the string is coerced to lowercase letters
        word = Word("Racecar")
        self.assertEqual(word.input_word, "racecar")

        # test errors for multi-word strings
        with self.assertRaises(ValueError):
            Word("racecar fast")

        # test value error for a list
        with self.assertRaises(ValueError):
            Word(["racecarracecaar"])

        # test value error for a numeric input 
        with self.assertRaises(ValueError):
            Word(1)

    def test_populate_stack(self):
        '''test to ensure that stacks are being populated properly'''

        # test basic stack functionality 
        stack = Stack()

        word = Word("for")
        word.populate_stack("for", stack)

        self.assertEqual(stack.pop(), "r")
        self.assertEqual(stack.pop(), "o")
        self.assertEqual(stack.pop(), "f")

        # ensure an error is raised if the stack is empty and we try to
        # pop another element 
        with self.assertRaises(IndexError):
            stack.pop()

    def test_populate_queue(self):
        '''test to ensure that stacks are being populated properly'''

        # test basic stack functionality 
        queue = Queue()

        word = Word("for")
        word.populate_queue("for", queue)

        self.assertEqual(queue.dequeue(), "f")
        self.assertEqual(queue.dequeue(), "o")
        self.assertEqual(queue.dequeue(), "r")

        # ensure an error is raised if the stack is empty and we try to
        # pop another element 
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_split_string(self):
        '''test to ensure that the split_string works as expected'''

        word = Word("forfor")
        queue = Queue()
        queue.enqueue(word.input_word)

        word.split_string(queue, 2)

        # ensure we have two "for" elements and then an empty queue
        self.assertEqual(queue.dequeue(), "for")
        self.assertEqual(queue.dequeue(), "for")

        # ensure an error is raised if the stack is empty and we try to
        # pop another element 
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_is_palindrome(self):
        '''test to ensure is_palindrome is identifying palindromes'''

        # test a non-palindrome
        word = Word("forfor")
        self.assertFalse(word.is_palindrome())

        # test a single palindrome
        word = Word("racecar")
        self.assertTrue(word.is_palindrome())

        # test a multi palindrome
        word = Word("racecarracecar")
        self.assertTrue(word.is_palindrome())

        # test a multi palindrome
        word = Word("racecarracecar")
        self.assertTrue(word.is_palindrome(2))

        # test a multi palindrome
        word = Word("racecarracecarracecarracecar")
        self.assertTrue(word.is_palindrome(3))

    def test_is_repeat(self):
        '''ensure is_repeat is identifying repeat words'''

        # test a non-palindrome repeat
        word = Word("forfor")
        self.assertTrue(word.is_repeat())

        # test a non-repeat word
        word = Word("racecar")
        self.assertTrue(word.is_repeat())

        # test a non-repeat word
        word = Word("racecar")
        self.assertFalse(word.is_palindrome(2))

        # test a multi palindrome
        word = Word("racecarracecar")
        self.assertTrue(word.is_repeat(2))

        # test a multi palindrome
        word = Word("racecarracecarracecarracecar")
        self.assertTrue(word.is_repeat(4))

        # test a multi palindrome
        word = "jmgukndhemmehdnkugmjjmgukndhemmehdnkugmjjmgukndhemmehdnkugmj"
        word = Word(word)
        self.assertTrue(word.is_repeat(3))




if __name__ == "__main__":
    unittest.main()