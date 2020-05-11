def maximumIncreasingSubsequence(array): 
    sequence = [None for _ in range(len(array))] 
    sums = array[:] 
    maxIdx = 0 
    for i in range(1, len(array)): 
        currentNumber = array[i] 
        for j in range(i):
            traverseNumber = array[j] 
            if traverseNumber < currentNumber and sums[j] + currentNumber > sums[i]: 
                sums[i] = sums[j] + currentNumber 
                sequence[i] = j 
        if sums[i] >= sums[maxIdx]:
            maxIdx = i

    returnSeq = list()
    iterNum = maxIdx 
    while iterNum >= 0: 
        returnSeq.append(array[iterNum])
        iterNum = sequence[iterNum]
        if iterNum is None: break 

    return [sums[maxIdx], list(reversed(returnSeq))]



input = [10, 70, 20, 30, 50, 11, 30]
print(maximumIncreasingSubsequence(input))
             

