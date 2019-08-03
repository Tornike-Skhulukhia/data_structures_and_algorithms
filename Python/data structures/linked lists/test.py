'''
    test singly-linked lists functionality
'''

from singly_linked_lists import Node
import random

# starting points location
head = Node(1)


#############################
# add elements
for i in range(2, 100):
    head.append(Node(random.randint(1, 101)))

#############################
print("All available node values".center(30), "="*30, sep="\n")
head.print_all_nodes(0)


# test index
print("="*30, "Checking random numbers".center(30), sep="\n")

for i in random.sample(range(20), 10):
    print(f'Number {i:<3} - returned index {head.index(i):>3} ')
