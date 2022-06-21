# problem link -> https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.sols = []
        board = [["." for _ in range(n)] for _ in range(n)]
        self.solve(board, 0)
        return self.sols

    def isvalid(self, board, row, col):
        n = len(board)
        for i in range(n):
            if board[i][col] == 'Q':
                return False
            if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 'Q':
                return False
            if row - i >= 0 and col + i <n and board[row-i][col+i] == 'Q':
                return False
            
        return True

    def solve(self, board, row):
        if row == len(board):
            ans = []
            for i in range(len(board)):
                ans.append("".join(board[i]))
            self.sols.append(ans)
            return

        for col in range(len(board)):
            if self.isvalid(board, row, col):
                board[row][col] = 'Q'
                self.solve(board, row+1)
                board[row][col] = '.'