def longest_palindrome(string):
    left = 0
    right = len(string) - 1
    l_p = []
    curr = []

    while left < right:
        if string[left] == string[right]:
            curr.append(string[left])
        else:
            l_p = l_p if len(l_p) >= len(curr) else curr
            curr = []

        left += 1
        right -= 1

    return ''.join(l_p)

input = "abaxyzzyxf"
longest_palindrome(input)