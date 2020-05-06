# O(N log N) time and O(log N) space (average and best)
# O(N^2) time worst case 
def quickSort(array): 
    quickSortRecursive(array, 0, len(array) - 1)
    return array 

def quickSortRecursive(array, startIdx, endIdx): 
    if startIdx >= endIdx: return 

    pivot = array[startIdx]

    i = startIdx + 1 
    for j in range(startIdx + 1, endIdx + 1): 
        if array[j] < pivot:
            swap(j, i, array)
            i += 1 

    swap(i - 1, startIdx, array)
    quickSortRecursive(array, startIdx, i - 2)
    quickSortRecursive(array, i, endIdx)

def swap(i, j, a): 
    a[i], a[j] = a[j], a[i]

input = [8, 5, 2, 9, 5, 6, 3, 1]

print(quickSort(input))
