'''
    Hardest algorithm in the universe,
    please do not try to repeat at home

    Linear Search.
'''

def get_index(array, elem):
    '''
    return -1, if element is not in array,
    otherwise, return its index
    '''
    for index, elem_ in enumerate(array):
        if elem_ == elem:
            return index
    return -1


# tests - copied from binary search file(- sort) 
# hand tests
arrays = [
        # full array                           # search     # correct answer    
        {"array": [],                          "elem": 9,     "correct": -1},
        {"array": [1, 2, 3],                   "elem": 2,     "correct":  1},
        {"array": [1, 8, 9, 90, 123],          "elem": 1,     "correct":  0},
        {"array": [1, 3, 7, 9, 24, 98, 431],   "elem": 431,   "correct":  6},
        {"array": [1, 3, 7, 9, 24, 99, 431],   "elem": 2,     "correct": -1},
        {"array": [1, 3, 7, 9, 24, 99, 431],   "elem": 502,   "correct": -1},
]
answers = [1 if get_index(i["array"], i["elem"]) == i["correct"]
                                                else 0 for i in arrays]
assert all(answers)

# random tests
import random

for i in range(100):
    array = random.sample(range(1000), 50)
    elem = random.randint(1, 1000)
    answer = get_index(array, elem)

    if elem in array:
        assert array.index(elem) == answer
    else:
        assert answer == -1