# O(N) time and O(N) space 
def productExceptSelf(nums): 
    nElem = len(nums)
    leftProd = [1] * nElem 
    rightProd = [1] * nElem 

    # building leftProd 
    for i in range(1, nElem):
        # multiply the observed product so far to the left of i and the number to the left of i 
        leftProd[i] = leftProd[i - 1] * nums[i - 1] 

    # building rightProd 
    for i in reversed(range(nElem - 1)): 
        rightProd[i] = rightProd[i + 1] * nums[i + 1]

    return list(map(lambda x, y: x * y, leftProd, rightProd))

# O(N) time and O(1) space 
def prodExceptSelf(nums): 
    nElem = len(nums)
    output = [1] * nElem 

    for i in range(1, nElem): 
        output[i] = output[i - 1] * nums[i - 1] 

    runningProd = 1 
    for i in reversed(range(nElem)):
        output[i] *= runningProd 
        runningProd *= nums[i]
        
    return output 

print(productExceptSelf([1, 2, 3, 4]))



