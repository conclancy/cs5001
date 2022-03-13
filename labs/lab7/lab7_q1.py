'''def count_by_fives(ending_value):

    # if not isinstance(ending_value, list):
    #    ending_value = [ending_value]

    if  ending_value <= 0:
        return [0]
    else:
        current_value = ending_value - 5
        values_list = count_by_fives(current_value)
        values_list = values_list.append(current_value)

    return values_list
'''


def test_count_by_fives_recursive(ending_value):
    '''
    test_count_by_fives_recursive is willtest the count_by_fives_recursive.
    the expected outcome from the two functions should be the same.
    '''

    # local vairables 
    result = []
    count = 0

    # generate list in increments of 5
    while count <= ending_value:
        result.append(count)
        count += 5

    # return results
    return result


def count_by_fives_recursive(ending_value):

    if ending_value < 0:
        return []

    if ending_value < 5:
        return [0]
    else: 
        values_list = count_by_fives_recursive(ending_value - 5)
        values_list.append(values_list[-1] + 5)

    return values_list


if __name__ == "__main__":
    value = int(input("Enter multiple of five: "))
    print(count_by_fives_recursive(value))


# tests, 