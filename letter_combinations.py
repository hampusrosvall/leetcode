class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return ""
        phoneChars = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']} 
        result = list()

        self.backTrack("", digits, result, phoneChars)
        return result 

    def backTrack(self, tempString, digits, result, lookUp): 
        if not len(digits): 
            result.append(tempString)
            return 
        
        for char in lookUp[digits[0]]: 
            self.backTrack(tempString + char, digits[1:], result, lookUp)