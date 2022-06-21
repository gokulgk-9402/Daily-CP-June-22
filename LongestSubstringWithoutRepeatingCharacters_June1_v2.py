# problem link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      # this is a more efficient approach using sliding window
        max = 0
        charSet = set()

        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

            if len(charSet) >= max:
                max = len(charSet)
            
            if l >= len(s) - max:
                break

        return max