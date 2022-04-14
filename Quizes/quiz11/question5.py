''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Quiz 11 - Question 5
clancy.co@northeastern.edu (002781018)
14 April 2022

The file contains a program that allows the user to create a stack ADT
'''

class Stack:
    '''
    The stack class is an ADT that allows users to store and access items 
    in a LIFO manner. 
    '''

    def __init__(self):
        self.data = list()
 
    def push(self, item):
        '''
        the push function adds an item to the stack
        params: a string item
        returns: Void
        '''
        self.data.append(item)


    def  pop(self):
        '''
        the pop function returns the last item and removes it from the stack
        returns: Void
        '''
        self.data.pop()
    
    def dump(self):
        '''
        dump returns the values in the stack from top to bottom
        returns: a single string for each item in the stack
        '''

        for i in range(len(self.data) - 1, -1, -1):
            print(self.data[i])

if __name__ == "__main__":

    # initalize the stack 
    quiz_stack = Stack()

    # Add 5 items to the stack 
    for n in range(5):
        quiz_stack.push(n)
    
    print(quiz_stack.dump())

    # remove 3 items from the stack
    for n in range(3):
        quiz_stack.pop()
    
    print(quiz_stack.dump())
