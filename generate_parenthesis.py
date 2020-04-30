class Solution:
    def generateParenthesis(self, n: int):
        results = list()
        self.backTrack("", results, 0, 0, n)

        return results 

    def backTrack(self, tempString, results, open, closed, max): 
        if len(tempString) == 2 * max: 
            results.append(tempString)
            return 

        if open < max: self.backTrack(tempString + '(', results, open + 1, closed, max)
        if closed < open: self.backTrack(tempString + ')', results, open, closed + 1, max)


sol = Solution()
print(sol.generateParenthesis(3))
