class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "" or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)

            maxlen = max(len1, len2)

            if maxlen > end - start:
                start = i - (maxlen-1)//2
                end = i + maxlen//2
        # print(start, end)
        return s[start:end+1]

    def expandAroundCenter(self, s: str, left: int, right: int):
        L = left
        R = right
        while L>= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R-L-1