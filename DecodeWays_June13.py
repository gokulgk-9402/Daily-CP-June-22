# problem link -> https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        prev1, prev2 = 1, 1
        
        for i in range(1, len(s)):
            if s[i] == '0':
                if s[i-1] + s[i] in ('10', '20'):
                    cur = prev1
                else:
                    return 0
                
            else:
                if 11<= int(s[i-1] + s[i]) <= 26:
                    cur = prev1 + prev2
                else:
                    cur = prev2
                    
                
            prev1 = prev2
            prev2 = cur
                
        return cur