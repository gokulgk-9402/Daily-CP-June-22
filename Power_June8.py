# problem link -> https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def dp(n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n % 2:
                num = dp(n//2)
                return num * num * x
            else:
                num = dp(n//2)
                return num * num

        return dp(n) if n > 0 else 1/dp(-n)