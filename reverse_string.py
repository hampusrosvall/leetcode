""" 
Time: O(N) as we are performing \frac{N}{2} swaps 
Space: O(1) as we are not allocating any extra memory to perform in-place swaps 
 
"""

def reverse_string(string):
    if len(string) < 2: 
        return string

    left = 0 
    right = len(string) - 1

    while left < right: 
        string[left], string[right] = string[right], string[left]
        left += 1 
        right -= 1 

    return string 

input  = list("hello")

print(reverse_string(input))
    
