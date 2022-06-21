# proble link -> https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxindex = 0

        for index, num in enumerate(nums):
            if index > maxindex:
                return False

            maxindex = max(num + index, maxindex)

        return True