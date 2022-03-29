def main():
    '''main function for program'''

    # create variables
    words = {
        'hello': 'a commono greeting', 
        'world': 'the planet we live on', 
        'exceed': 'to do great',
        'quiz': 'a test of knowledge',
        'immutable': 'cannot be changed'}

    # iterate over keys and values of dictionary
    for word, definition in words.items():

        # print the key and value if the key doesn't start with an e
        if word[0] != 'e':
            print(word, "--", definition)


main()
