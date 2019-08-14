'''
    Peak finder using simple linear approach
'''


def get_peak_index(array):
    '''
    return peak if exits, -1 otherwise
    '''
    for index, elem in enumerate(array):
        left = array[index - 1] if index != 0 else elem
        right = array[index + 1] if index != (len(array) - 1) else elem

        if left <= elem >= right:
            return index
    return -1


# test
print(get_peak_index([12, 23, 34]))
