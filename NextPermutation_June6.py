# problem link -> https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums[:]
        temp.sort(reverse=True)
        if temp == nums:
            nums = nums.sort()
            return
        
        i = len(nums) - 1

        while i > 1 and nums[i-1] >= nums[i]:
            i -= 1
            
        toswap1 = i-1

        while i < len(nums) and nums[i] > nums[toswap1]:
            i += 1
        just_max_pos = i-1
        t = nums[toswap1]
        nums[toswap1] = nums[just_max_pos]
        nums[just_max_pos] = t
        t = nums[toswap1+1:]
        t.reverse()
        for i in range(len(t)):
            nums[toswap1+i+1] = t[i]