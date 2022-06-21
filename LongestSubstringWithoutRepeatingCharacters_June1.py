# problem link -> https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:      # this is a brute force approach
        max = 0
        for i in range(len(s)):
            longeststr = ''
            for j in range(i, len(s)):
                if s[j] in longeststr:
                    break
                longeststr += s[j]
            if len(longeststr) > max:
                max = len(longeststr)
                
        return max