def main(): 
    '''
    Takes in two numbers and an operator, returing the operation on the inputs. 
    '''

    first_number = float(input("Input first number:"))
    second_number = float(input("Input second number:"))
    operator = input("Input operator (+,-,*,/):")

    if second_number == 0:
        print("NaN")
    elif operator == "+":
        print(first_number, "+", second_number, "=", first_number + second_number)
    elif operator == "-":
        print(first_number, "-", second_number, "=", first_number - second_number)
    elif operator == "*":
        print(first_number, "*", second_number, "=", first_number * second_number)
    elif operator == "/":
        print(first_number, "/", second_number, "=", first_number / second_number)
    else:
        print("Invalid operator. Please use +,-,*,/. ")


main()