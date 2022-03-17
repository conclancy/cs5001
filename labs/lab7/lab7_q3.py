''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 7 - Question 2 (Multiples of 5 Again)
clancy.co@northeastern.edu (002781018)
16 MAR 22 

The file contains a function that takes in a single number and returns a list
with all of the multples of 5 less than or equal to that value
'''


def filter_list (input_list, threshold):
    '''
    filter_list takes in a list of numbers and a threshold and returns the
    numbers in the list that are less than the threshold.
    :params: a list and an int. 
    :return: a list of numbers less than the threshold
    '''

    if not input_list:
        return []

    if input_list[0] > threshold:
        value_list = filter_list(input_list[1:], threshold)
        value_list.append(input_list[0])
        return sorted(value_list)
    else:
        value_list = filter_list(input_list[1:], threshold)
        return sorted(filter_list(input_list[1:], threshold))


if __name__ == "__main__":
    print(filter_list([1,2,3,4], 0))