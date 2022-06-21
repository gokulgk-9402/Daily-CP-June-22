# problem link -> https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transp = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
        return transp