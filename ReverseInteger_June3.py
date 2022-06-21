# problem link -> https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
        while x!=0:
            reversed *= 10
            reversed += x%10
            if reversed <= -2**31 or reversed >= 2**31 -1:
                return 0
            x = x//10
        return reversed * sign