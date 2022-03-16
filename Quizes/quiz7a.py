def numbers(number):
    '''
    Takes in an integer and recursively prints all numbers to 1
    :params int: single int number
    :returns: None, prints multiple single-line strings
    '''

    if number == 0: 
        print("Done!")
    else:
        print(number)
        numbers(number - 1)

def main():
    numbers(int(input("Input a number:")))

main()