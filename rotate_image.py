class Solution:
    def rotate(self, v: List[List[int]]) -> None:
        self.transpose(v)
        
        endRow = len(v)
        endCol = len(v[0])
        
        for row in range(endRow):
            left, right = 0, endCol - 1 
            while left < right: 
                v[row][left], v[row][right] = v[row][right], v[row][left]
                left += 1 
                right -= 1 
        
    def transpose(self, m) -> None: 
        for i in range(len(m)): 
            for j in range(i, len(m[0])):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        