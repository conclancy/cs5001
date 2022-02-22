''' CS5001.38359.202230 - SEC 05 - John Wilder
    Lab 5 - Problem 2 (Budget)
    clancy.co@northeastern.edu (002781018)
    22 FEB 22 

    This file takes in a budget and a list of prices and removes
    items you cannot afford from the list 
'''


def within_budget(prices_list, budget):
    '''
    removes prices over the budget from the list
    params: list of floats and a single float
    returns: list of floats
    '''
    
    # create function variables
    i = 0
    budget_list = []

    # iterate over every element in the list
    while i < len(prices_list):
        price = prices_list[i]

        # add prices <= the budget into the new cleaned list
        if price <= budget:
            budget_list.append(price)

        # increment iterator 
        i += 1
    
    # return the list of items within budget
    return budget_list


def main():
    '''
    tests the within_budget() functon to ensure it is functioning as expected
    '''

    # Create test variables 
    i = 0
    tests_passed = 0
    tests_failed = 0

    '''
    t[0] = price list
    t[1] = budget
    t[2] = expected outcome
    '''
    test_list = [[[1, 2, 3], 2, [1, 2]]]

    while i < len(test_list):
        if within_budget(test_list[i][0], test_list[i][1]) == test_list[i][2]:
            tests_passed += 1
        
        i += 1

    print(tests_passed)

main()