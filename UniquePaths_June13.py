# problem link -> https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mem = {}
        def dp(m, n):
            if m==1 or n == 1:
                return 1
            
            if not mem.get((m,n), None):
                mem[(m,n)] = dp(m-1, n) + dp(m, n-1)
             
            return mem[(m,n)]
        
        return dp(m,n)