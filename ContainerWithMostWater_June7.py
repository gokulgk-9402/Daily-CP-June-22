# problem link -> https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        # min_height = min(height[left], height[right])
        max_vol = 0
        
        while left < right:
            
            max_vol = max(max_vol, min(height[left], height[right]) * (right - left))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
        return max_vol
        