def dailyTemperatures(T): 
    stack = []
    daysUntilWarmer = [0] * len(T)

    for i, temp in enumerate(T): 
        while stack and T[stack[-1]] < temp: 
            prevIdx = stack.pop() 
            daysUntilWarmer[prevIdx] = i - prevIdx 
        stack.append(i)

    return daysUntilWarmer 

input = [73, 74, 75, 71, 69, 72, 76, 73]

print(dailyTemperatures(input))