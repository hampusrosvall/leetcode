def longest_substring(string): 
    i, j = 0, 0 
    longest = [i, j]
    hash_map = dict()

    while j < len(string): 
        char = string[j]
        if char in hash_map: 
            i = max(hash_map[char], i)
        
        hash_map[char] = j + 1 
        longest = max(longest, [i, j], key = lambda x: x[1] - x[0]) 
        j += 1 

    left_idx = longest[0]
    right_idx = longest[1] + 1 
    return string[left_idx:right_idx]

input = "clementisacap"
print(longest_substring(input))

""" 
    {c:1, l:2, e:3, m:4}
    "clementisacap"
        i 
          j


""" 