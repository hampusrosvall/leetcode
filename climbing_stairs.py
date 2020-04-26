"""
Time: O(N)
Space: O(N)

"""

def climbStairs(n: int) -> int: 
    # check for base cases 
    if n == 1: return 1 
    if n == 2: return 2 

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n - 1] 

input = 4 

print(climbStairs(input))
