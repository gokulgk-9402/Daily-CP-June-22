# problem link -> https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        
        def lcs(s1, s2, m, n):
            if m==0 or n ==0:
                return 0
            if memo[m][n] > 0:
                return memo[m][n]
            if s1[m-1] == s2[n-1]:
                memo[m][n] = 1 + lcs(s1, s2, m-1, n-1)
            else:
                memo[m][n] = max(lcs(s1, s2, m, n-1), lcs(s1, s2, m-1, n))
                
            return memo[m][n]
        
        return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2))