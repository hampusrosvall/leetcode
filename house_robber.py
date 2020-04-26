""" 
Time: O(N)
Space: O(N)

To easily solve this question we use the technique of dynamic programming i.e., applying past knowledge to solve future problems. 

Since are not allowed to rob any two adjacent houses due to the risk of getting caught, and we want to maximize the "profit". 
Thus, at each house h we compare if the current highest profit available at the previous house is greater than the profit we can 
gain by robbing this house and the maximum profit of a house one or more steps away.  

Hence, the logic applied at each house h is 

maxProfit[h] = max(maxProfit[h -1], maxProfit[h -2] + currentProfit[h])

We are thus storing an extra array of length N -> O(N) space and we scan the input array once -> O(N) time.

""" 

def houseRobber(array): 
    if not len(array): 
        return 0 
    elif len(array) == 1: 
        return array[0]

    maxGains = array[:]
    maxGains[1] = max(array[0], array[1])

    for i in range(2, len(array)): 
        maxGains[i] = max(maxGains[i - 1], maxGains[i - 2] + array[i]) 

    return maxGains[-1]


input = [1,2]

print(houseRobber(input))