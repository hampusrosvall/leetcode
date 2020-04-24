""" 
The trick is to keep a seperate pointer to where the "first" zero to be swapped is at. 
Initialize the index to zero and it will keep incrementing if we pass non-zero numbers. 

Time: O(N) as we scan through the entire array 
Space: O(1) as we allocate no extra space for this solution

""" 

def move_zeroes(nums):
    index = 0  # to keep track of the current index where we have a zero 
    N = len(nums)
    for i in range(N): 
        if nums[i]: 
            if i != index: swap(index, i, nums)
            index += 1 
    return nums 

def swap(i, j, array): 
    array[i], array[j] = array[j], array[i]

input = [0, 1, 0, 3, 12]
#input = [1, 2, 0, 3]

print(move_zeroes(input))
