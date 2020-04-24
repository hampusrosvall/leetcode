"""
Time: O(N)
Space: O(N)

Basically, we allocate O(N) extra memory to keep track of which numbers are visisted in an array. 
This could also be done with a HashMap or similar. 
"""

def find_missing(nums): 
    N = len(nums)
    visited_nbrs = [0] * N 

    for num in nums: 
        visited_nbrs[num - 1] = 1 

    missing_nbrs = []
    for index, _ in enumerate(visited_nbrs): 
        if not visited_nbrs[index]: 
            missing_nbrs.append(index + 1)

    return missing_nbrs 

""" 
Constant space solution: 
Idea is to perform a linear scan and calculate the actual index of each element.
Mark that element at that index with a negative sign to mark its existence. 
Lastly, return all the indicies + 1 whose element is not negative. 

[4,3,2,7,8,2,3,1] -> [-4,-3,-2,-7,8,2,-3,-1]
                                  ^ ^
                                missing elements 
"""

def constant_space_fm(nums): 
    for elem in nums: 
        actual_sorted_idx = abs(elem) - 1
        nums[actual_sorted_idx] = -1 * abs(nums[actual_sorted_idx])

    missing_numbers = []
    for index, elem in enumerate(nums): 
        if elem > 0: 
            missing_numbers.append(index + 1)

    return missing_numbers

        

input = [4,3,2,7,8,2,3,1]

print(find_missing(input))
print(constant_space_fm(input))