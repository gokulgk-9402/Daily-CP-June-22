# problem link -> https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        next_row = triangle[-1][:]
        current_row = [0] * len(triangle)
        
        for i in range(len(triangle) -2, -1, -1):
            for j in range(i+1):
                left = next_row[j] + triangle[i][j]
                right = next_row[j+1] + triangle[i][j]
                current_row[j] = min(left, right)
                
            next_row, current_row = current_row, next_row
            
        return next_row[0]