'''
    selection sort
'''
import random

# array = [2, 5, 1, 6, 3]



def sort_it(array):

    for index in range(len(array) - 1):

        min_index = index

        for i in range(index + 1, len(array)):
            if array[i] < array[min_index]:
                min_index = i
        array[min_index], array[index] = array[index], array[min_index]

    return array



# test 
for i in range(100):
    array_ = random.sample(range(1000), 100)
    print(array_)
    array = sort_it(array_[:])
    print(array)

    assert array == sorted(array_)
