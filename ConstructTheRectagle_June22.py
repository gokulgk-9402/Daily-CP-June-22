# problem link -> https://leetcode.com/problems/construct-the-rectangle/

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        rt = area ** 0.5
        
        if rt.is_integer():
            return [int(rt), int(rt)]
        
        length = int(rt) + 1
        while True:
            if not area%length:
                return [int(length), area//length]
            length += 1
            
        