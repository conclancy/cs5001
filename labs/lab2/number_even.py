''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 2 - Problem 1
    clancy.co@northeastern.edu (002781018)
    03 FEB 22 
'''


def main(input_number):
    '''
    Takes in a number and determines if it is even or odd.
    '''

    if input_number % 2 == 0:
        print(input_number, "is even")
    else:
        print(input_number, "is odd")


if __name__ == "__main__":
    input_number = int(input("Input number: "))
    main(input_number)
