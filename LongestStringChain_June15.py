# problem link -> https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        ans = 1

        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dp:
                    dp[word] = dp[pred] + 1
                    ans = max(ans, dp[word])

        return ans