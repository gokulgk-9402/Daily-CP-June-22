# problem link -> https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        # here dp(i,j) denotes if t[i:] and p[j:] match, hence dp(0,0) denotes if t and p match
        # and we are storing it in memory dictionary with (i,j) tuple as keys
        
        def dp (i, j):
            if (i, j) not in memory:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j +1 <len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j) 
                    else:
                        ans = first_match and dp(i+1, j+1)

                memory[(i,j)] = ans
            return memory[(i,j)]

        return dp(0,0)