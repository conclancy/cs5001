''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 8 - Readability
clancy.co@northeastern.edu (002781018)
26 MAR 22 

The file calculates the Flesch Index and Flesch Grade Level for a text file
'''


def analyze_file_data(file_data):
    '''
    Function: analyze_file_data
        Calculates the number of sentences, words, and syllabues in file_data
    Parameters:
        file_data -- the data to analyze
    Returns the number of sentences (int), the number of words (int),
        and the number of syllables in file_data
    '''

    # variables 
    word_list = []
    words = 0
    sentences = 0
    syllables = 0

    for nested_list in file_data:
        for element in nested_list.split():
            word_list.append(element)

    # set word count 
    words = len(word_list)

    # count the number of sentences in the file data and return the word list
    # without punctuation for syllabul evaluation
    sentences, clean_word_list = punctuation_handler(word_list)

    # count the number of syllables in the sentence 
    for word in clean_word_list:
        syllables = syllables + count_syllables(word)

    return sentences, words, syllables


def punctuation_handler(word_list):
    '''
    Function: punctuation_handler
        Calculates the number of sentences, and removes punctuation from list
    Parameters:
        word_list -- a list of words to analyze
    Returns: number of sentences (int), list of words without puncuation (list)
    '''

    # constants
    PUNCTUATION = [".", "?", "!", ":", ";"]

    # variables
    word_count = 0
    punctuation = 0
    return_words = []

    # iterate through each word in the list
    for word in word_list: 

        # count the number of words 
        word_count = word_count + 1

        # create a blank bariable called new string to store the string without
        # punctuation
        new_string = ""

        # iterate over each character in the string
        for character in word:

            # count the number of punctuation marks 
            if character in PUNCTUATION: 
                punctuation = punctuation + 1

            # append all non-punctuation characters to the new_string
            elif character.isalnum():
                new_string = new_string + character

        # add the punctuatio-free string to the return word list
        return_words.append(new_string)

    return punctuation, return_words


def count_syllables(word):
    '''
    Function: count_syllables
        Counts the total number of syllables in the provided word
    Parameters:
        word -- the word that we want to count the syllables of
    Returns the number of syllables in the word
    '''

    # standardize the letters to be lower case
    word = word.lower()

    # constants 
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    syllables = 0 

    # don't count strings of just spaces
    if word.isspace():
        return 0

    # vowel work
    if word[0] in vowels:
        syllables = syllables + 1

    # iterate through the word and increase the syllables count by one if the
    # letter is a vowel and the preceeding vowel is not a vowel 
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            syllables = syllables + 1

    # if the final letter is an 'e', then 
    if word[-1] == 'e' and word[-2] not in vowels:
        syllables = syllables - 1

    # all words have at least one syllable, return 1 if count is less than 1
    if syllables < 1:
        syllables = 1

    return syllables


def flesch_index(sentences, words, syllables):
    '''
    Function: flesch_index
        calculates the Flesch readability index
    Parameters:
        sentences (int) -- the number of sentences in a document
        words (int) -- the number of words in a document
        syllables (int) -- the number of syllables
    Returns the Flesch readability index calculated by the provided formula
    '''

    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)


def flesch_grade(index):
    '''
    Function: flesch_grade
        Caclulates the Flesch grade (educational level)
    Parameters:
        index (float) -- Flesch readability index
    Returns the educational level
    '''

    # mat the index to return a grade
    if index < 0: 
        return "Law school graduate"
    elif index < 30:
        return "College graduate"
    elif index < 50:
        return "College"
    elif index < 65:
        return "High schooler"
    elif index < 70:
        return "8th Grader"
    elif index < 80:
        return "7th Grader"
    elif index < 90:
        return "6th Grader"
    elif index <= 100:
        return "5th Grader"
    else:
        return None


def main():
    """ The main driver of the program. """

    # Ask user for name of file to analyze.
    filename = input("Filename: ")

    try:
        file = open(filename, "r") 
    except FileNotFoundError: 
        print(filename, "does not exist")
    except PermissionError: 
        print("You do not have sufficient permissions to open", )
    except OSError:
        print("An unexpected error occurred while attempting to open", 
              filename)

    # Open file for reading.
    input_file = open(filename, 'r')

    # Read all of the contents of the file
    # into a list of strings called filedata.
    filedata = input_file.readlines()

    # Analyze the data from the file to calculate
    # the number of sentences, the number of words
    # and the number of syllables in the file
    sentences, words, syllables = analyze_file_data(filedata)
    index = flesch_index(sentences, words, syllables)
    grade = flesch_grade(index)

    # Close the file.
    input_file.close()

    # Output result.
    print()
    print("Syllables:", syllables)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Words per Sentence: {0:.1f}".format(words / sentences))
    print("Syllables per Word: {0:.1f}".format(syllables / words))
    print()
    print("Flesch Index: {0:.1f}".format(index))
    print("Flesch Grade:", grade)


if __name__ == '__main__':
    main()
