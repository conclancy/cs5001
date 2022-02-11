''' CS5001.38359.202230 - SEC 05 - John Wilder
    Quiz 3 - Question 5
    clancy.co@northeastern.edu (002781018)
    08 FEB 22 
'''

def word_integer(integer, word):
    '''
    word_integer
    param: integer int, word str
    return: bool
    '''

    if integer == 1 and word == "one":
        return True 
    elif integer == 2 and word == "two":
        return True
    elif integer == 3 and word == "three": 
        return True 
    elif integer == 4 and word == "four":
        return True 
    elif integer == 5 and word == "five": 
        return True 
    else: 
        return False

def main():

    # Variable inputs 
    integer = int(input("Enter integer value: "))
    word = input("Enter word: ")

    # call function 
    word_match_integer = word_integer(integer, word.lower())

    # final output
    if word_match_integer:
        print(str(integer), "and", word, "are the same number")
    elif not word_match_integer: 
         print(str(integer), "and", word, "are NOT the same number")

main() 