# problem link -> https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1, int2 = 0, 0
        for character in num1:
            int1 = int1 * 10 + int(character)
        for character in num2:
            int2 = int2 * 10 + int(character)

        if int1 == 0 or int2 == 0:
            return "0"
        
        int1 *= int2
        ans = []
        while int1 > 0:
            ans.append(chr(int1%10 + 48))
            int1 //= 10
            
        ans.reverse()
        return ''.join(ans)