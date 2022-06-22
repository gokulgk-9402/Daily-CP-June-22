# problem link -> https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dp(nums, target, i, curr):
            key = (i, curr)
            if key in memo:
                return memo[key]

            if i == len(nums):
                if curr == target:
                    return 1

                else:
                    return 0

            add = dp(nums, target, i+1, curr + nums[i])
            sub = dp(nums, target, i+1, curr - nums[i])

            memo[key] = add + sub

            return memo[key]

        return dp(nums, target, 0, 0)