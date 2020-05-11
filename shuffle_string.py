import random 

def shuffle(input): 
    chars = list(input) # O(N) memory 
    upperBound = len(chars) - 1 
    output = list()

    for _ in range(len(chars)):
        sampleIdx = random.randint(0, upperBound)
        output.append(chars[sampleIdx])
        swap(chars, sampleIdx, upperBound)
        upperBound -= 1

    return ''.join(output) 


def swap(a, i, j): 
    a[i], a[j] = a[j], a[i]

print(shuffle('ab'))