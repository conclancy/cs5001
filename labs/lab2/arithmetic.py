''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 2 - Problem 2
    clancy.co@northeastern.edu (002781018)
    03 FEB 22 
'''


def main(first_number, second_number, operator): 
    '''
    Takes in two numbers and an operator, returing the operation on the inputs. 
    '''

    if second_number == 0:
        print(first_number, "/", int(second_number), "=", 
              "NaN")
    elif operator == "+":
        print(first_number, "+", second_number, "=", 
              first_number + second_number)
    elif operator == "-":
        print(first_number, "-", second_number, "=", 
              first_number - second_number)
    elif operator == "*":
        print(first_number, "*", second_number, "=", 
              first_number * second_number)
    elif operator == "/":
        print(first_number, "/", second_number, "=", 
              first_number / second_number)
    else:
        print("Invalid operator. Please use +,-,*,/. ")


if __name__ == "__main__":
    first_number = float(input("Input first number: "))
    second_number = float(input("Input second number: "))
    operator = input("Input operator (+,-,*,/): ")
    main(first_number, second_number, operator)
