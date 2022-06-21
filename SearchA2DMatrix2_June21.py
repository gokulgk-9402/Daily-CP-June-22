# problem link -> https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows ==0 and cols == 0:
            return False

        def BS(row):
            left = 0
            right = cols -1

            while(left<=right):
                mid = left + (right-left)//2

                if matrix[row][mid] == target:
                    return True

                if matrix[row][mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return False

        for i in range(rows):
            if BS(i):
                return True

        return False