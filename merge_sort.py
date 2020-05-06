def mergeSort(array): 
    if len(array) == 1: return array 

    middle = len(array) // 2 

    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    
    return merge(left, right)

def merge(left, right): 
    leftSize, rightSize = len(left), len(right) 

    result = [None] * (leftSize + rightSize)
    leftPointer, rightPointer = 0, 0
    idx = 0 

    while leftPointer < leftSize and rightPointer < rightSize: 
        if left[leftPointer] <= right[rightPointer]: 
            result[idx] = left[leftPointer]
            leftPointer += 1 
        else: 
            result[idx] = right[rightPointer]
            rightPointer += 1 
        
        if leftPointer == leftSize: 
            result[leftPointer + rightPointer:] = right[rightPointer:]
            break 
        
        if rightPointer == rightSize: 
            result[leftPointer + rightPointer:] = left[leftPointer:]
            break 

        idx += 1

    return result 

input = [8, 5, 2, 9, 5, 6, 3, 1]

print(mergeSort(input))