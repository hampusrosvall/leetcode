import heapq 

def kthLargest(nums, k): 
    nLargest = heapq.nlargest(k, nums) 
    return nLargest[-1]


nums = [3,2,1,5,6,4]
k = 2 
kthLargest(nums, k)