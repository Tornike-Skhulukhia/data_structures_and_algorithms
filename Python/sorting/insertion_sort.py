'''
    Insertion sort
'''

import random
# array = [1, 5, 3, 8, 2]

def sort_it(array):

    for curr_elem_index in range(1, len(array)):
        curr_elem = array[curr_elem_index]

        previous_index = curr_elem_index - 1

        while previous_index >= 0 and array[previous_index] > curr_elem:
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1
        array[previous_index + 1] = curr_elem

    return array

# test
array_ = random.sample(range(1000), 20)

print(array_)
array = sort_it(array_)
print(array)

print(sorted(array_) == array)