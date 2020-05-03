import collections 
# brute force O(d log d) where d is the # of unique elements in nums and O(d) space (hash map + three lists)
class Solution:
    def topKFrequent(self, nums, k) -> list:
        intCount = collections.defaultdict(int)
        
        for num in nums: 
            intCount[num] += 1 

        counts = list() 
        numbers = list()

        for number, count in intCount.items(): 
            counts.append(count)
            numbers.append(number)

        sortedNbrs = [nbr for _,nbr in sorted(zip(counts, numbers), key = lambda x : x[0], reverse = True)]

        return sortedNbrs[:k]

sol = Solution()
ans = sol.topKFrequent([1,1,1,2,2,3], 2)
print(ans)