# problem link -> https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = 1
        digits[n-i] += 1
        while digits[n-i] >= 10 and i < n:
            digits[n-i] = digits[n-i] % 10
            digits[n-i-1] += 1
            i += 1
            
        if digits[0] >= 10:
            digits[0] %= digits[0]
            return [1] + digits
        
        return digits