# problem link -> https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        mem = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    mem[i] = max(mem[i], mem[j] + 1)

        result = max(mem)

        return result
        
