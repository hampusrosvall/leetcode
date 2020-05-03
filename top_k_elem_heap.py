import collections 

class MaxHeap: 
    def __init__(self, array): 
        self.heap = self.buildHeap(array) 

    def buildHeap(self, array):
        parentIdx = (len(array) - 1) // 2 

        while parentIdx >= 0: 
            self.bubbleDown(array, parentIdx, len(array) - 1)
            parentIdx -= 1 

        return array 

    def bubbleDown(self, heap, startIdx, finishIdx): 
        childOne = 2 * startIdx + 1 

        while childOne <= finishIdx: 
            childTwo = childOne + 1 if childOne + 1 <= finishIdx else None 

            if childOne and childTwo: 
                largestIdx = childOne if heap[childOne]['value'] >= heap[childTwo]['value'] else childTwo 
                if heap[largestIdx]['value'] > heap[startIdx]['value']:
                    self.swap(heap, startIdx, largestIdx)
                    startIdx = largestIdx
                    childOne = 2 * startIdx + 1 
                else: 
                    return  

            else:
                if heap[childOne]['value'] > heap[startIdx]['value']: 
                    self.swap(heap, startIdx, childOne)
                    startIdx = childOne 
                    childOne = 2 * startIdx + 1 
                else: 
                    return 
    def swap(self, array, i, j): 
        array[i], array[j] = array[j], array[i]

    def pop(self): 
        self.swap(self.heap, 0, len(self.heap) - 1)
        nbr = self.heap.pop() 

        self.bubbleDown(self.heap, 0, len(self.heap) - 1)

        return nbr 

# O(N) time and O(D) space 
def topKFrequent(nums, k): 
    # O(N) frequency count 
    nbrFreq = collections.Counter(nums) 

    # O(D) storage of the frequencies (D -> # unique numbers)
    nbrFreqArray = list()

    for key, value in nbrFreq.items(): 
        nbrFreqArray.append(
            {'number': key, 'value': value}
        )

    # O(D) build MaxHeap operation 
    heap = MaxHeap(nbrFreqArray)

    topFreqNbrs = list() 

    # perform k O(log(D)) operations (bubbleDown has O(log D) time complexity) 
    for _ in range(k): 
        topFreqNbrs.append(heap.pop()['number'])

    return topFreqNbrs

nums = [1,1,1,2,2,3]
k = 2 

print(topKFrequent(nums, k))


    




