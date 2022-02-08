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
     
    # 400-999 logic   
    if number_remainder >= 900:
        number_remainder -= 900
        roman += "CM"
    elif number_remainder >= 500:
        number_remainder -= 500
        roman += "D"
    elif number_remainder >= 400:
        number_remainder -= 400
        roman += "CD"
    
    # 100 - 399 logic 
    if number_remainder >= 100:
        hundreds_int = number_remainder // 100
        roman += "C" * hundreds_int
        number_remainder = number_remainder - (hundreds_int * 100)

    # 50 - 99 Logic 
    if number_remainder >= 90:
        number_remainder -= 90
        roman += "XC"
    elif number_remainder >= 50:
        number_remainder -= 50
        roman += "L"
    elif number_remainder >= 40:
        number_remainder -= 40
        roman += "XL"
    
    # 10 - 39 Logic 
    if number_remainder >= 10:
        hundreds_int = number_remainder // 10
        roman += "X" * hundreds_int
        number_remainder = number_remainder - (hundreds_int * 10)
    
    # 5 - 9 Logic 
    if number_remainder >= 9:
        number_remainder -= 9
        roman += "IX"
    elif number_remainder >= 5:
        number_remainder -= 5
        roman += "V"
    elif number_remainder >= 4:
        number_remainder -= 4
        roman += "IV"
    
    # 1 - 3 Logic 
    if number_remainder >= 1:
        hundreds_int = number_remainder // 1
        roman += "I" * hundreds_int

    # Print Answer 
    print(roman)
    

if __name__ == "__main__":
    number = int(input("Input first number: "))
    main(number)
    
