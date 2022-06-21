# problem link -> https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        mem = []

        def cands(n):
            if n <= len(mem):
                return mem[n-1]

            if n == 1:
                mem.append("1")
                return "1"
            
            num = cands(n-1)
            
            i = 1
            digit = num[0]
            count = 1
            ans = ""
            while i < len(num):
                if digit == num[i]:
                    count += 1
                else:
                    ans+= str(count)
                    ans+= str(digit)
                    count = 1
                    digit = num[i]
                    
                i += 1

            ans += str(count)
            ans += str(digit)
            mem.append(ans)
            return ans

        return cands(n)