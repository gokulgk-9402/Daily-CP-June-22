# problem link -> https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        last_filled = 0
        
        while i < len(chars):
            cur = chars[i]
            count = 0
            
            while chars[i] == cur:
                i += 1
                count += 1
                if i >= len(chars):
                    break
                
            if count == 1:
                chars[last_filled] = cur
                last_filled += 1
            else:
                chars[last_filled] = cur
                last_filled += 1
                ls = list(str(count))
                for el in ls:
                    chars[last_filled] = el
                    last_filled += 1
            
        return last_filled