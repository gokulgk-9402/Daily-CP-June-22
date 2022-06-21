# problem link -> https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsums = []
        if len(nums) >= 1:
            runningsums.append(nums[0])
        for i in range(1, len(nums)):
            runningsums.append(runningsums[-1] + nums[i])
            
        return runningsums