"""
The idea behind the solution is that we, for each temperature that is greater than the follwing days temperature, 
we append its index to the a stack. As soon as we encounter a temperature that is greater than the previous days temperature, 
we pop the last index from the stack and calculate the difference in position in the list for all elements in the stack. 

Algorithm: 
first iteration: 
stack = [0]
[0, 0, 0, 0, 0, 0, 0, 0]
[73, 74, 75, 71, 69, 72, 76, 73]
 0   1   2   3   4   5    6   7 
 ^

second iteration: 
T[1] > T[0] so we pop the first index from the stack and calculate the difference between 1 - 0 = 1 
[1, 0, 0, 0, 0, 0, 0, 0]
[73, 74, 75, 71, 69, 72, 76, 73]
 0   1   2   3   4   5    6   7 
     ^

 Append 1 to the stack -> stack [1]

third iteration: 
T[2] > T[1] so we pop the first index from the stack and calculate the difference between 2 - 1 = 1 
[1, 1, 0, 0, 0, 0, 0, 0]
[73, 74, 75, 71, 69, 72, 76, 73]
 0   1   2   3   4   5    6   7 
         ^

 Append 2 to the stack -> stack [2]

 fourth iteration: 
 T[3] !> T[1] so we append 3 to the stack -> stack = [2, 3]
[1, 1, 0, 0, 0, 0, 0, 0]
[73, 74, 75, 71, 69, 72, 76, 73]
 0   1   2   3   4   5    6   7 
             ^

firth iteration: 69 < 71 so we append 4 to the stack -> stack = [2, 3, 4]
sixth iteration: 72 > 69 so we pop 4 from the stack and update the dailyTemperatures array. Then we pop 3 from the stack and update. 




""" 

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