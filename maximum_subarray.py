def maximum_subarray(array):
    N = len(array) 
    sums = [float('-inf')] * N 
    rolling_sum = 0 
    for idx, nbr in enumerate(array): 
        rolling_sum += nbr 
        sums[idx] = rolling_sum 

        if rolling_sum < 0: 
            rolling_sum = 0 

    return max(sums)         
        

""" 
    [0   0   0  0   0  0  0   0  0]
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]

""" 


input = [-2,1,-3,4,-1,2,1,-5,4]
print(maximum_subarray(input))