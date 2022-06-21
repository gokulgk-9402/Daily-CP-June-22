# problem link -> https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        i = 0
        while i <= len(s)/2:
            if s[i] != s[-1-i]:
                return 2
            i += 1
        return 1
