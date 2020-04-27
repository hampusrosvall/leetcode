""" 
input: [7, [1, 5, 10]]
output: 3 (2x1 + 1x5)

denom = 5: 
 0  1  2  3  4  5  6 
[1, 2, 3, 4, 1, 6, 7]
 1  2  3  4  5  6  7 
""" 

def minNumberOfChange(n, denoms): 
    numOfCoins = [float('inf') for _ in range(n + 1)]
    numOfCoins[0] = 0 
    for denom in denoms: 
        for amount in range(n + 1): 
            if denom <= amount: 
                numOfCoins[amount] = min(numOfCoins[amount], 1 + numOfCoins[amount - denom])

    return numOfCoins[-1] if numOfCoins[-1] != float('inf') else -1 

n = 3 
denoms = [2, 1]

print(minNumberOfChange(n, denoms))          

    