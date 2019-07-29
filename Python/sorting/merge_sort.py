'''
    Merge sort using python, 
    attempt N1 (working)
'''
import time
import random

# sort it
def sort_it(array, v=True):
    try:
        if len(array) < 2:
            # base case
            if v: print("returned:", array)
            return array

        else:
            # recursive part
            # sort left half
            left = sort_it(array[: len(array) // 2], v)
            # sort right half
            right = sort_it(array[len(array) // 2 :], v)
            # merge them
            merged = []

            left_p  = 0
            right_p = 0

            while left_p < len(left) and right_p < len(right):
                left_ = left[left_p] 
                right_ = right[right_p] 

                if left_ < right_:
                    merged.append(left_)
                    left_p += 1
                else:
                    merged.append(right_)
                    right_p += 1

            # check which part caused break and add other fully
            if right_p >= len(right):
                # if right is fully done, add left remainings
                merged.extend(left[left_p: ])
            else:
                merged.extend(right[right_p: ])


            if v:  print("left:" , left, "right:", right, "merged:", merged)
            return merged
    except:
        import traceback; print(traceback.format_exc())    
        import pdb; pdb.set_trace()


# test
# array = [3, 12, 6, 123, 2] 
for i in range(10):

    array = random.sample(range(1000000), 1000)

    # print("Initial array: ", array, "\n", "="*80, sep="")
    # measure time
    time.sleep(0.1)
    t_1 = time.time()
    result = sort_it(array, v=False)
    diff_1 = time.time() - t_1
    # print("="*80, "\nresult:", result)

    time.sleep(0.1)
    t_2 = time.time()
    python_sorted = sorted(array)
    diff_2 = time.time() - t_2

    print(f'Our solution: {diff_1:.7f} seconds, builtin sort: {diff_2:.7f} '
          f'seconds, {diff_1 / diff_2:.3f} times faster')

    assert python_sorted == result
