def analyze_file_data(file_data):
    '''
    Function: analyze_file_data
       Calculates the number of sentences, words, and syllabues in file_data
    Parameters:
       file_data -- the data to analyze
    Returns the number of sentences (int), the number of words (int),
       and the number of syllables in file_data
    '''
    sentences = 0
    words = 0
    syllables = 0

    # TODO: Implement me!

    return sentences, words, syllables


def count_syllables(word):
    '''
    Function: count_syllables
       Counts the total number of syllables in the provided word
    Parameters:
       word -- the word that we want to count the syllables of
    Returns the number of syllables in the word
    '''
    # TODO: implement me!


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
    # TODO: Implement me!!


def main():
    """ The main driver of the program. """
    # Ask user for name of file to analyze.
    filename = input("Filename: ")

    # TODO: Modify this function to handle any errors raised by the
    #       file handling.

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
