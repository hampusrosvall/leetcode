def stock(prices): 
    profit = float('-inf')
    buy = prices[0]  
    for i in range(1, len(prices)):
        sell = prices[i]
        profit = max(profit, sell - buy) 

        if prices[i] < buy: 
            buy = prices[i]

    return profit

input = [7, 5, 6, 1, 4]
print(stock(input))


