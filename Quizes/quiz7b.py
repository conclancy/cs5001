def make_palindrome(sequence, check_character = -1):
    '''
    make_palindrome takes in a sequence and doubles the length returning
    the input sequence forwards and then backwards. The check_character 
    variable should not be set when first calling the function and left 
    to default to -1. 
    :params str: a single string
    :returns str: a single string that is a palindrome of input string.
    '''

    # if this is the first recursion, set the check_character param to the 
    # length of the sequence - 1 to call the last character next. 
    if check_character < 0:
        make_palindrome(sequence, len(sequence) - 1)

    # if this is the first character in the sequence, append it to the end
    # and print the statement to end the function. 
    elif check_character == 0:
        sequence = sequence + sequence[check_character]
        print(sequence)

    # else, append the check character to the end of the string, decrement the
    # check_character param and call the next recursion.
    else:
        sequence = sequence + sequence[check_character]
        make_palindrome(sequence, check_character - 1)

make_palindrome("super")