def main():
    '''
    Takes in a number and determines if it is even or odd. 
    '''
    
    number = int(input("Enter an integer to determine if it is even or odd:"))

    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


main()