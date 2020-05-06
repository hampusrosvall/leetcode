def minimumPathCost(grid): 
    nRows, nCols = len(grid), len(grid[0])
    cheapestPath = [[0 for _ in range(nCols)] for _ in range(nRows)]
    cheapestPath[0][0] = grid[0][0]
    for col in range(1, nCols): 
        cheapestPath[0][col] = cheapestPath[0][col - 1] + grid[0][col]

    for row in range(1, nRows): 
        cheapestPath[row][0] = cheapestPath[row - 1][0] + grid[row][0]

    for row in range(1, nRows): 
        for col in range(1, nCols): 
            cheapestPath[row][col] = grid[row][col] + min(cheapestPath[row][col - 1], cheapestPath[row - 1][col])

    return cheapestPath[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

print(minimumPathCost(grid))

