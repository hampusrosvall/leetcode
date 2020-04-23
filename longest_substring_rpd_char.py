# O(N) time and O(N) space 
def longest_substring(string): 
    i, j = 0, 0 
    hash_map = dict()
    longest = 0 
        
    while j < len(string): 
        if string[j] in hash_map: 
            # update pointer i to point to the right of the char s[j]
            i = max(hash_map[string[j]], i)
        
        # update pointer to character s[j]
        hash_map[string[j]] = j + 1 
        longest = max(longest, j + 1 - i)
        j += 1
            
    return longest  

input = "abba"
print(longest_substring(input))
""" 
    {a:1, b:3}
    longest = 2
     0123
    "abba" 
       i
        j

    "dvdf" 
      i
        j
""" 