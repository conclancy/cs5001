''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 9 - Scrabble
clancy.co@northeastern.edu (002781018)
29 MAR 22 

The file finds all possible words for a scrabble game given a list of letters
and the desired word length of the word.
'''


import os
import string
import sys


def read_text_file():
    '''
    Function -- read_text_file
        Returns the content of the file "wordlist.txt"
    Parameters:
        None
    Returns the contents of the file as a list of strings
    Raises a ValueError if any errors occur while reading the file
        with the message "Error occurred reading the word list"
    '''

    # try and load the wordfile and return it to the caller
    try:
        # use the path of the current file to find the wordlist.txt file
        input_file = open(os.path.join(sys.path[0], 'wordlist.txt'), 'r')
        file_data = input_file.readlines()
        input_file.close()
        return file_data
    except FileNotFoundError or PermissionError or OSError:
        raise ValueError("Error occurred reading the word list")
    


def store_words(file_data):
    '''
    Function -- store_words
        Returns words separated according to their lengths.
    Parameters:
        file_data -- a list of strings containing the words to be sorted
    Returns a dictionary where the key is the word length, and the value
        is all of the words in file_data that of that length
    '''

    # create empty dictionary to store keys and words
    dictionary = {}

    for word in file_data:

        # remove the new line character from the strings
        word = word.replace('\n', '')

        # if the key exists, add the word to its list, otherwise add a key
        # to the dictionary and add the word as the first word in the value 
        # list
        try: 
            dictionary[len(word)].append(word)
        except KeyError:
            dictionary[len(word)] = [word]

    return dictionary



def interpret_input(data):
    '''
    Function -- interpret_input
        Identifies the letters and number of results to be displayed
        from the user input.
    Parameters:
        data -- string with user response
    Returns the number of highest scoring words to display
        and the letters the word should contain
    '''
    if not isinstance(data, str):
        raise TypeError("interpret_input is expecting a string parameter")

    outputs = ''
    letters = ''
    for i in data:
        # Identify letters
        if i in string.ascii_lowercase:
            letters += i
        # Identify number of results to be displayed
        if i in string.digits:
            outputs += i
    outputs = int(outputs)
    return outputs, letters


def get_words(max_length, word_dict, letters):
    '''
    Function -- get_words
        Returns the words that contain the letters specified by the user.
    Parameters:
        letters -- letters that the words should contain
        word_dict -- With length of words as key and the words as values
        max_length -- maximum length of the word to be displayed
    Returns a list of words containing the user input letters
    '''

    # create variables
    key_list = []
    filtered_words = []
    
    # create a list of relevant word lengths
    for key in word_dict.keys(): 
        if key <= max_length:
            key_list.append(key)

    # order the list so we search the dictionary in order
    key_list.sort()

    # for each word length
    for key in key_list:

        # for each word of the key length
        for word in word_dict[key]: 

            # creat a variable to assume all desired letters are in word
            append_word = True 

            # test each desired letter, if its not in the word, change the 
            # append_word variable to false
            for letter in letters: 
                if letter not in word: 
                    append_word = False

            # if append_word is true, add the word to the filtered list
            if append_word:
                filtered_words.append(word)

    return filtered_words

def get_scores(words):
    '''
    Function -- get_scores
        Calculates the score for each word that contains the letters specified
        by the user and then displays 'n' highest scoring words;
        'n' being the number specified by the user.
    Parameters:
        words -- List of words containing the user input letters
    Returns a dictionary containing the points as keys and the words as values
    '''
    
    # create dictionary constant for letter score
    LETTER_SCORE = {
        "a": 1,
        "b": 3, 
        "c": 3, 
        "d": 2,
        "e": 1,
        "f": 4, 
        "g": 2,
        "h": 4, 
        "i": 1,
        "j": 8, 
        "k": 5,
        "l": 1,
        "m": 3, 
        "n": 1, 
        "o": 1, 
        "p": 3, 
        "q": 10, 
        "r": 1, 
        "s": 1, 
        "t": 1, 
        "u": 1, 
        "v": 4, 
        "w": 4, 
        "x": 8, 
        "y": 4, 
        "z": 10}

    # create variable to store scored words
    scored_words = {}

    # iterate through the list of input words
    for word in words:

        # create a loop variable to store word score
        word_score = 0 

        # iterate through the letters and score each one
        for letter in word: 
            word_score = word_score + LETTER_SCORE[letter]

        # if the key exists, add the word to its list, otherwise add a key
        # to the dictionary and add the word as the first word in the value 
        # list
        try: 
            scored_words[word_score].append(word)
        except KeyError:
            scored_words[word_score] = [word]

    return scored_words


def print_scores(scores, number):
    '''
    Function -- print_scores
        Print the 'n' highest-scoring words based on their scrabble score
    Parameters:
        scores -- dictionary filled with points as keys and words as values
        number -- number of highest scoring words to display
    '''
    if not isinstance(scores, dict):
        raise TypeError("scrabble_scores is expecting a dictionary as the first parameter")
    if not isinstance(number, int):
        raise TypeError("scrabble_scores is expecting an integer as the second parameter")

    count = 1
    for key in sorted(scores, reverse=True):
        for item in sorted(scores[key]):
            if count != number + 1:
                print(count, item, key)
                count += 1


def get_new_length(cmd):
    '''
    Function -- get_new_length
        Get the new length
    Parameters:
        cmd -- the command to change the length
    Returns the new length
    '''
    if not isinstance(cmd, str):
        raise TypeError("get_new_length is expecting a string as a parameter")
    length = ''
    for i in cmd:
        if i in string.digits:
            length += str(i)
    max_length = int(length)
    return max_length


def main():
    ''' The program driver '''
    file_data = read_text_file()
    word_dict = store_words(file_data)
    max_length = 7

    cmd = input('> ')
    # Process user response
    while cmd != 'quit()':
        if cmd.startswith("len("):
            max_length = get_new_length(cmd)
        else:
            # Identify letters and number of results (n)
            # to display from user response
            outputs, letters = interpret_input(cmd)
            # Identify the words from wordlist.txt
            # that contain user input letters
            scrabble_word_lst = get_words(max_length, word_dict, letters)
            # Calculate the score for each word and add it to a dictionary
            # Tagging the score to the word
            scrabble_scores = get_scores(scrabble_word_lst)
            # Displays 'n' highest scoring words
            print_scores(scrabble_scores, outputs)

        # Get the user's next response if length is not changed
        cmd = input('> ')


if __name__ == '__main__':
    main()
