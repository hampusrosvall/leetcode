"""
'xyz', key: 2 -> zab
"""
def cce(string, key):
    n_shifts = key % 25
    shifted_string = []
    LOWER_BOUND = 97
    UPPER_BOUND = 122

    for char in string:
        ord_c = ord(char)
        new_c = (ord_c + n_shifts)

        if new_c > UPPER_BOUND:
            new_c = LOWER_BOUND + new_c % 122 - 1
        elif new_c < LOWER_BOUND:
            new_c = UPPER_BOUND - (LOWER_BOUND - new_c)

        shifted_string.append(chr(new_c))


    return ''.join(shifted_string)

print(cce('abc', -2))
