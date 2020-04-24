""" 
Time: O(N)
Space: O(N)
""" 

from collections import defaultdict

def majority(array): 
    elem_count = defaultdict(int)
    N = len(array) 

    for elem in array: 
        elem_count[elem] += 1 

    for key, value in elem.items(): 
        if value > N / 2: 
            return key 

"""

A possible solution is to sort the array in place i.e. O(1) space and then look up the middle element of the array. 

"""

