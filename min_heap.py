class MinHeap: 
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

        # bubble down until we reach the end of the heap 
        while childOne <= finishIdx: 
            # check if we also have second child present 
            if childOne + 1 <= finishIdx:
                childTwo = childOne + 1 
            else:
                childTwo = None 
            
            # find the smallest value of the two children nodes 
            if childOne and childTwo: 
                if heap[childOne] < heap[childTwo]: 
                    smallestIdx = childOne 
                else: 
                    smallestIdx = childTwo 
                
                if heap[smallestIdx] < heap[startIdx]:
                    self.swap(heap, smallestIdx, startIdx)
                    startIdx = smallestIdx 
                    childOne = 2 * startIdx + 1 
                else:
                    return 
            else: 
                if heap[childOne] < heap[startIdx]: 
                    self.swap(heap, childOne, startIdx)
                    startIdx = childOne 
                    childOne = 2 * startIdx + 1 
                else: 
                    return 

    def swap(self, array, i, j): 
        array[i], array[j] = array[j], array[i]


    def bubbleUp(self, heap, startIdx, finishIdx): 
        parentIdx = (startIdx - 1) // 2 

        while parentIdx >= finishIdx: 
            if heap[startIdx] < heap[parentIdx]: 
                self.swap(heap, startIdx, parentIdx)
                startIdx = parentIdx 
                parentIdx = (parentIdx - 1) // 2
            else: 
                return 

    def push(self, value): 
        self.heap.append(value) 
        self.bubbleUp(self.heap, len(array) - 1, 0)

    def pop(self): 
        self.swap(self.heap, 0, len(array) - 1)
        removedValue = self.heap.pop()  

        self.bubbleDown(self.heap, 0, len(array) - 1)

        return removedValue 

if __name__ == '__main__': 
    array = [17, 15, 9, 12, 10]
    myHeap = MinHeap(array)
    myHeap.push(1)
    myHeap.pop()
    print(myHeap.heap)
