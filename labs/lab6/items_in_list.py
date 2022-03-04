''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 6 - Problem 4 (Items in List)
    clancy.co@northeastern.edu (002781018)
    3 MAR 22 

    Contains a function that takes in two lists and returns a list of unique
    elements present in both lists.
'''


def items_in_list(list1, list2):
    '''
    Takes in two lists and returns a list that contains elements present in
    both lists. 

    params: two lists of ints
    returns: list of ints
    '''

    # create variables
    items_in_list = []

    # iterate through lists for matches
    for i in list1:
        if i in list2 and i not in items_in_list:
            items_in_list.append(i)

    return items_in_list


def main():
    '''
    Function to test the above number_greater_than function
    '''

    # create variables
    tests_passed = 0
    tests_failed = 0

    test_cases = [[[1, 3], [1, 2, 3, 5], [1, 3, 4]],
                  [[], [1, 2, 3, 4, 8], []], 
                  [[2, 3], [1, 2, 3], [5, 2, 6, 2, 3, 7, 2]], 
                  [[3, 2], [3, 2, 2, 3], [5, 2, 6, 2, 3, 7, 2]],
                  [[], [1, 2, 3], [4, 5, 6]]]

    for t in test_cases:

        # test each case and increment corresponding pass/fail variables
        if t[0] == items_in_list(t[1], t[2]):
            tests_passed += 1
        else:
            tests_failed += 1

    # return final results
    if tests_passed != len(test_cases):
        print("Tests failed", tests_failed, "and tests passed", tests_passed)
    else:
        print("All tests passed!")


main()
