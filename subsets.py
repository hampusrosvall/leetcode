# RECURSIVE
def powerset(array, idx = None): 
    if idx is None: 
        idx = len(array) - 1 
    elif idx < 0: 
        return [[]]

    currentElem = array[idx]
    subsets = powerset(array, idx - 1)

    for i in range(len(subsets)): 
        subsets.append(subsets[i] + [currentElem])

    return subsets 

# ITERATIVE 
def powerset(array): 
    subsets = [[]]

    for elem in array: 
        for i in range(len(subsets)): 
            subsets.append(subsets[i] + [elem])

    return subsets 

# both algortihms run in O(N2^N) space and memory 



print(powerset([1, 2, 3]))