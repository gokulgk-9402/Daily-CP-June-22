#problem link -> https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        distinct = 1
        i = 0
        while i < len(nums):
            if nums[i] != nums[distinct-1]:
                nums[distinct] = nums[i]
                distinct += 1
            i += 1
        
        return distinct