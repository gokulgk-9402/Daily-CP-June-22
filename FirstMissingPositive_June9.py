# problem link -> https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        setnums = set(nums)

        for i in range(1, len(nums) + 2):
            if i not in setnums:
                return i

        return i