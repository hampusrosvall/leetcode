def longestPalindrome(s): 
    longest_palindrome = ""
    for i in range(1, len(s) - 1): 
        odd = isPalindrome(i - 1, i + 1, s)
        even = isPalindrome(i - 1, i, s)

        longest_current = longestString(odd, even)
        longest_palindrome = longestString(longest_current, longest_palindrome)

    return longest_palindrome 

def longestString(i, j): 
    return max(i, j, key = lambda x : len(x))

def isPalindrome(l, r, s): 
    while l >= 0 and r <= len(s) - 1: 
        if s[l] != s[r]: 
            break 
        l -= 1 
        r += 1 
    return s[l + 1:r]

input = "rosvallabbarosvall"
print(longestPalindrome(input))