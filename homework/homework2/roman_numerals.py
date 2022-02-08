''' CS5001.38359.202230 - SEC 05 - John Wilder
    Homework 2 (Roman Numerals)
    clancy.co@northeastern.edu (002781018)
    07 FEB 22 
'''


def main(number): 
    '''
    Takes in a number and coverts it to a roman numeral 
    '''

    # Determine the number of thosands in the number 
    if number >= 1000:
        thosands_int = number // 1000
        roman = "M" * thosands_int
        number_remainder = number - (thosands_int * 1000)
    else:
        roman = ""
        number_remainder = number

    # 500 logic   
    if number_remainder >= 500:
        number_remainder -= 500
        roman += "D"

    # 100's logic 
    if number_remainder >= 100:
        hundreds_int = number_remainder // 100
        roman += "C" * hundreds_int
        number_remainder = number_remainder - (hundreds_int * 100)

    # 50 Logic 
    if number_remainder >= 50:
        number_remainder -= 50
        roman += "L"

    # 10's Logic 
    if number_remainder >= 10:
        tens_int = number_remainder // 10
        roman += "X" * tens_int
        number_remainder = number_remainder - (tens_int * 10)

    # 5 Logic 
    if number_remainder >= 5:
        number_remainder -= 5
        roman += "V"

    # 1's Logic 
    if number_remainder >= 1:
        ones_int = number_remainder // 1
        roman += "I" * ones_int

    # Print Answer 
    print(number, "is", roman)


if __name__ == "__main__":
    number = int(input("Enter number:"))
    main(number)
