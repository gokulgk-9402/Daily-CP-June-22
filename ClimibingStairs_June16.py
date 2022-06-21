# problem link -> https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1]
        
        def dp(n):
            if n < 0:
                return 0
            if n <= len(mem):
                return mem[n-1]
            
            mem.append(dp(n-1) + dp(n-2))
            return mem[n-1]
        
        return dp(n)