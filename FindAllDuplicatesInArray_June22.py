# problem link -> https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        length = len(nums)

        for i in range(length):
            x = nums[i] % (length+1)
            nums[x-1] += length+1

        ans = []

        for i in range(length):
            if nums[i] // (length+1) > 1:
                ans.append(i+1)

        return ans