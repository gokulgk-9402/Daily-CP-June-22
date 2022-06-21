# problem link -> https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
            if len(ans) == 0:
                return ""
            j = len(ans)
            while j>0:
                if ans[0:j] != strs[i][0:j]:
                    j -= 1
                else:
                    break
            ans = ans[0:j]
            
        return ans