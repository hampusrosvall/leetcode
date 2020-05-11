# Time O(MN), Space O(MN)
def levenstein(stringOne, stringTwo): 
    dp = [[i for i in range(len(stringOne) + 1)] for _ in range(len(stringTwo) + 1)]
    
    for j in range(len(stringTwo) + 1): 
        dp[j][0] = j 

    for row in range(1, len(stringTwo) + 1): 
        for col in range(1, len(stringOne) + 1): 
            if stringOne[col -1] == stringTwo[row - 1]: dp[row][col] = dp[row - 1][col - 1]
            else: dp[row][col] = min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col -1]) + 1

    return dp[-1][-1]

print(levenstein('abc', 'yabd'))

# Let's make it more memory efficient, space = O(min(M, N))
def levensteinMemoryEfficient(stringOne, stringTwo): 
    if len(stringOne) >= len(stringTwo): shortest, longest = stringTwo, stringOne 
    else: shortest, longest = stringOne, stringTwo 

    even = [i for i in range(len(shortest) + 1)]
    odd = [None for _ in range(len(shortest) + 1)]

    for row in range(1, len(longest) + 1): 
        if row % 2 == 1: 
            current = odd 
            previous = even 
        else: 
            current = even 
            previous = odd 
        current[0] = row 
        for col in range(1, len(shortest) + 1): 
            if shortest[col - 1] == longest[row - 1]: 
                current[col] = previous[col - 1] 
            else: 
                current[col] = min(current[col - 1], previous[col], previous[col - 1]) + 1 

    return even[-1] if not row % 2 else odd[-1]
            




print(levensteinMemoryEfficient('abc', 'yabd'))