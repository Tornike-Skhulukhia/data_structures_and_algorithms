'''
    Singly-linked lists
'''
'''
    useful Python's list functions to add:
        index
        in
    
        append
        prepend
        delete
        insert
        reverse
        ...
'''
import time

class Node:
    '''
    single node element
    '''
    def __init__(self, value):
        self.value = value
        self.points_to = None

    def __repr__(self):
        '''
        working method to quickly get just list if needed
        '''
        print(f"[")
        self.print_all_nodes(0, ',' )
        print("]")

        return None 

    def point_to(self, node):
        '''
        point node to other one
        '''
        self.points_to = node

    def append(self, node):
        '''
        get head element, follow its pointers and 
        append one more element at the end.
        '''
        # last_node = self

        # # get last element
        # while last_node.points_to is not None:
        #     last_node = last_node.points_to

        last_node = self.get_last_node()

        # add there
        last_node.point_to(node)

    def get_last_node(self):
        '''
        get first node, follow its next objects and return last one
        '''
        last_node = self

        while last_node.points_to is not None:
            last_node = last_node.points_to

        return last_node


    def index(self, value):
        '''
        if value is in list return its first occurence's index,
        -1 otherwise
        '''
        index = 0
        node = self

        while node.points_to is not None:
            if node.value == value:
                return index
            node = node.points_to
            index += 1
        # and last ones check
        return -1 if value != node.value else index


    def print_all_nodes(self, sleep_interval=0.4, end=" --> "):
        '''
        get first node and print all nodes after that
        '''

        # we can not print character at a time (?)
        # ! if sleep_interval is too hight and print has
        # not new line as end, we need to wait
        # for full line generation, so be careful...
        
        last_node = self

        # import pdb; pdb.set_trace()

        while last_node.points_to is not None:
            print(last_node.value, end=end)
            last_node = last_node.points_to
            
            time.sleep(sleep_interval)

        print(last_node.value)


