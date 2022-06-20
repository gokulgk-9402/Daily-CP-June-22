# problem link -> https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 2*n + 0.25
        ans = ans ** 0.5
        ans -= 0.5
        return int(ans)