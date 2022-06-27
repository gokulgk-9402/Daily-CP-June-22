# problem link -> https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 11:
            return []
        
        mem = {}
        for i in range(len(s) - 9):
            window = s[i:i+10]
            if window in mem:
                mem[window] += 1
            else:
                mem[window] = 1
                
        res = []
        for key in mem.keys():
            if mem[key] > 1:
                res.append(key)
                
        return res