def spread_string(string_list):
    '''
    Takes in a list of strings and prints each word on a seperate line
    with a space between each letter in the word. 
    params: list of str
    returns: str
    '''

    for s in string_list:

        # create an empty string to store values
        word_string = ''

        # for each letter in the word, append to word_string and 
        # seperate it from the next letter with a space 
        for letter in s:
            word_string = word_string + letter + ' '

        # remove the final space
        word_string = word_string.rstrip()

        # print the word
        print(word_string)


def main():
    spread_string(['Connor', 'and', 'Saleh'])


main()