''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Quiz 12 - Question 6
clancy.co@northeastern.edu (002781018)
21 April 2022

The file contains a program that sorts a list of numbers and retruns only 
the odd values.
'''

import random

def odd_numbers(nums):
    '''
    Function: odd_numbers -- sorting the elements of a list by inserting
                            each element into a list in order if it is odd
    Parameters:
       cards -- the elements to be sorted
    Returns a new list with all of the elements in sorted order
    '''
    # base case is just a single card
    if len(nums) == 1:

        # only return odd numbered cards
        if nums[0] % 2 != 0:
            return nums
        else:
            return []

    else:
        # find the midpoint of this
        mid = len(nums) // 2
        # sort the cards in the first half of the deck
        sorted_top = odd_numbers(nums[0:mid])
        # sort the cards in the second half of the deck
        sorted_bottom = odd_numbers(nums[mid:])
        # merge them together and regurn
        return merge(sorted_top, sorted_bottom)

def merge(deck1, deck2):
    '''
    Function: merge -- merge two sorted lists together in sorted order
    Parameters:
       deck1 -- the first sorted list
       deck2 -- the second sorted list
    Returns a new list that contains all of the elements of deck1 and deck2
    '''
    i1 = 0
    i2 = 0
    merged = []
    while i1 < len(deck1) and i2 < len(deck2):
        # pick the lowest card from the top of the two decks
        if deck1[i1] < deck2[i2]:
            merged.append(deck1[i1])
            i1 += 1
        else:
            merged.append(deck2[i2])
            i2 += 1
    # if one of the decks runs out, just add the rest of them
    if i1 < len(deck1):
        merged.extend(deck1[i1:])
    else:
        merged.extend(deck2[i2:])
    return merged


if __name__ == "__main__":
    '''
    Function: main -- driver program for merge_sort
    '''
    my_list = [i for i in range(100)]
    random.shuffle(my_list)
    print(my_list)
    sorted_list = odd_numbers(my_list)
    print(sorted_list)