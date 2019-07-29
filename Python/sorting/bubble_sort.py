# bubble sort algorithm
import random

# array = [9,  4,  2, 12,  8]
array = random.sample(range(1000),  10)


def sort_it(array):
	
	swaps = -1
	
	while swaps:
		swaps = 0
		
		for index in range(len(array) - 1):
			if array[index] > array[index + 1]:
				array[index + 1], array[index] = array[index], array[index + 1]
				swaps += 1

	return array

print(array)
array = sort_it(array)
print(array)


print(array == sorted(array))