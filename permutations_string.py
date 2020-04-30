""" 

input = "abc" 


""" 

def generatePermutations(string): 
    results = []
    permutations("" ,string, results)
    return results 

def permutations(prefix, suffix, results): 
    if not len(suffix): 
        results.append(prefix)
        return

    for i in range(len(suffix)): 
        permutations(prefix + suffix[i], suffix[:i] + suffix[i + 1:], results)


print(generatePermutations("abc"))
    



    

