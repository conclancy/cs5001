def main():
    '''
    Sorts three numbers in ascending order
    '''

    # Create variables 
    input_first_number = float(input("Input first number:"))
    input_second_number = float(input("Input second number:"))
    input_third_number = float(input("Input third number:"))

    # Logic if the first number is larger than the second
    if input_first_number >= input_second_number:
        output_largest_number = input_first_number

        # Logic if the second number is larger than the third number 
        # We know the order of the numbers (1, 2, 3)
        if input_second_number >= input_third_number:
            output_middle_number = input_second_number
            output_smallest_number = input_third_number

        # Test to see if the third is the largest number 
        elif input_third_number >= input_first_number:
            output_largest_number = input_third_number
            output_middle_number = input_first_number
            output_smallest_number = input_second_number

        # Logic if the third number is larger than the second, but smaller than the first
        else:
            output_middle_number = input_third_number 
            output_smallest_number = input_second_number

    # Logic if the second number is larger than the first
    else: 
        output_largest_number = input_second_number

        # Logic if the first number is larger than the third. 
        if input_first_number >= input_third_number:
            output_middle_number = input_first_number
            output_smallest_number = input_third_number

        # Test to see if the third is the largest number 
        elif input_third_number >=  input_second_number:
            output_largest_number = input_third_number
            output_middle_number = input_second_number
            output_smallest_number = input_first_number
        
        # Default logic if the third number is the middle largest. 
        else: 
            output_middle_number = input_third_number 
            output_smallest_number = input_first_number

    print(output_smallest_number, ",", output_middle_number, ",", output_largest_number)


main()