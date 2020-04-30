def generatePermutations(numbers): 
    results = list()
    permutations(list(), numbers, results) 

    return results 

def permutations(tempList, numbers, results): 
    if len(tempList) == len(numbers): 
        results.append(tempList.copy())
        return 

    for i in range(len(numbers)): 
        if numbers[i] in tempList: continue 
        tempList.append(numbers[i])
        permutations(tempList, numbers, results)
        tempList.pop()

input = [1, 2, 3]

print(generatePermutations(input))