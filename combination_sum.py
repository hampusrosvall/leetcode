def combinationSum(numbers, target): 
    combinations = list()
    numbers.sort() 
    backTrack(combinations, list(), target, numbers)

    return combinations

def backTrack(combinations, candidate, remainding, numbers): 
    if not remainding: 
        combinations.append(candidate.copy())
        return  

    for index, num in enumerate(numbers): 
        if num > remainding: break 
        candidate += [num] 
        backTrack(combinations, candidate, remainding - num, numbers[index:])
        candidate.pop()

input = [8,7,4,3]

print(combinationSum(input, 11))



    
            