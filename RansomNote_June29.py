# problem link -> https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_rn = Counter(ransomNote)
        counter_mag = Counter(magazine)
        
        for key in counter_rn.keys():
            val = counter_mag.get(key)
            val = val if val is not None else 0
            if counter_rn[key] > val:
                return False
        return True
         