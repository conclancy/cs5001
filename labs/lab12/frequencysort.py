''' 
CS5001.38359.202230 - SEC 05 - John Wilder
Lab 12 - Sorting
clancy.co@northeastern.edu (002781018)
22 APR 22 

This file contains a function that can take in list of integers
and sort it by the frequency of the items in the list
'''


def sort(unsorted_list) -> list:
    '''
    sort takes in a list of unsorted integers and returns the list
        sorted by frequency and initial value index
    params:
        unsorted_list = a list of integers 
    returns:
        list sorted by frequency in unsorted_list and index
    '''

    # function variables 
    values_dict = dict()
    index = 0
    freq = []
    output_list = []

    # identify frequency and initial index of numers in input list
    for i in unsorted_list:
        try:
            values_dict[i]['frequency'] += 1
        except KeyError:
            values_dict[i] = {'frequency': 1, 'index': index}

    # create a unique list of frequencies to create new list with
    for key in values_dict.keys():
        freq.append(values_dict[key]['frequency'])

    freq = sorted(list(set(freq)), reverse=True)

    # for each frequency
    for f in freq:
        freq_dict = dict()

        # determine value key pairs to process by frequency
        # an append them to the dictionary
        for key in values_dict.keys():
            if values_dict[key]['frequency'] == f:
                freq_dict[key] = values_dict[key]

        # get a unique list of initial indes from input list
        indexes = []
        for d in freq_dict.keys():
            indexes.append(freq_dict[d]['index'])

        # sorted the indexes in ascending order 
        indexes = sorted(indexes)  

        # for each index 
        for i in indexes:

            # for each key in the fre_dict 
            for key in freq_dict.keys():

                # prevent duplicate writes to list
                if key not in output_list:

                    # if value's frequency matches
                    if freq_dict[key]['index'] == i:

                        # append the item to the list the number of times it 
                        # appeard in the initial input list
                        for r in range(freq_dict[key]['frequency']):
                            output_list.append(key)

    return output_list


if __name__ == '__main__':
    '''main function'''

    num = ['o', 'C', 'C', 'n']

    print(sort(num))
