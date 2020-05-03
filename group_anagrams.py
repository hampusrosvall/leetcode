import collections 
def groupAnagrams(strs): 
    anagramMap = collections.defaultdict(list)

    for word in strs: 
        sortedWord = ''.join(sorted(word))
        anagramMap[sortedWord].append(word)
    return list(anagramMap.values())

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(input))
