''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 10 - Books
clancy.co@northeastern.edu (002781018)
03 APR 22 

The file contains the book class
'''
import os
import string
import sys
from readability import * 


class Book:
    '''
    The book class represents a book
    attributes: ISBN, title, author, year, formart, filename
    methods: get_title, get_athor, get_year, get_format, get_filename,
             get_readability_grade, get_index
    '''

    def __init__(self, isbn, title, author, year, format, filename) -> None:

        if isinstance(isbn, str):
            self.isbn = isbn
        else: 
            raise ValueError('Invalid ISBN provided to this Book')

        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError('Invalid title provided to this Book')

        if isinstance(author, str):
            self.author = author
        else: 
            raise ValueError('Invalid author provided to this Book')

        if isinstance(year, int):
            self.year = year
        else:
            raise ValueError('Invalid year provided to this Book')

        if isinstance(format, str):
            self.format = format
        else:
            raise ValueError('Invalid format provided to this Book')

        if isinstance(filename, str):
            self.filename = filename
        else:
            raise ValueError('Invalid filename provided book')

        self.readability = self.get_readibility_grade()


    def __str__(self) -> str:
        output = self.title + " by " + self.author + ", " + str(self.year) \
                 + "\n" + "ISBN: " + self.isbn + ", " + self.readability \
                 + ", " + self.filename
        
        return output


    def get_title(self) -> str:
        '''
        get_title method returns the the title of the book.
        params: self 
        returns: a single string 
        '''

        return self.title


    def get_athor(self) -> str:
        '''
        get_athor method returns the author of the book
        params: self
        returns: a single string
        '''

        return self.author


    def get_year(self) -> int:
        '''
        get_year method returns the year of the book
        params: self
        returns: a single int
        '''

        return self.year


    def get_format(self) -> str:
        '''
        get_format method returns the format of the book
        params self
        returns a single string
        '''

        return self.format


    def get_filename(self) -> str:
        '''
        get_filename method returns the filename of the book
        params self
        returns a single string
        '''

        return self.filename


    def read_file(self) -> str:
        '''
        read_file reads in the text for this book
        params self
        returns a single string
        '''

        file = open(os.path.join(sys.path[0], self.filename), 'r')

        return file


    def get_index(self) -> dict:
        '''
        get_index opens the 
        '''

        try:
            # create function variables
            index = {}
            words = []

            # iterate through the lines of the file
            for line in self.read_file():

                # iterate through each element in the line
                for element in line.split():

                    # create a variable to holder the elements letters
                    word = ''

                    # for each character in the element, append it to the word if 
                    # it is actually a letter 
                    for e in element: 
                        e = e.lower()
                        if e in string.ascii_lowercase:
                            word += e

                    # append the word to the word list
                    words.append(word)

            # for every word in the word list
            for w in words:

                # if the word is already in the dictionary, increment the value
                # by 1, if not, add the word to the dictionary with a value of 1
                try:
                    index[w] = index[w] + 1
                except:
                    index[w] = 1

            return index
        
        except:
            e = 'Error occurred while generating the index for' + \
                self.title
            raise ValueError(e)

    def get_readibility_grade(self) -> str:
        '''
        get_readibility_grade determines the readability grade for the book
        params self
        returns a single string 
        '''

        try:
            # Open file for reading.
            file = self.read_file()

            # Read all of the contents of the file
            # into a list of strings called filedata.
            filedata = file.readlines()

            # Analyze the data from the file to calculate
            # the number of sentences, the number of words
            # and the number of syllables in the file
            sentences, words, syllables = analyze_file_data(filedata)
            index = flesch_index(sentences, words, syllables)
            grade = flesch_grade(index)

            return grade

        except:
            e = 'Error occurred while calculating the Flesch grade for' + \
                self.title
            raise ValueError(e)

if __name__ == "__main__":

    print("\n")

    book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                "Hardcover", "catinthehat.txt")

    print(book.get_readibility_grade())