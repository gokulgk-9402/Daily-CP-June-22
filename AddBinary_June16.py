# problem link -> https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i1 = int(a, 2)
        i2 = int(b, 2)
        
        return str(bin(i1+i2))[2:]