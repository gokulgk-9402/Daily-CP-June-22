# problem link -> https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) <= 1:
            return [nums]
        for permutation in self.permute(nums[1:]):
            for i in range(len(nums)):
                ans.append(permutation[:i] + [nums[0]] + permutation[i:])
                
        return ans