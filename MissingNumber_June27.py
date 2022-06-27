# problem link -> https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        list_sum = sum(nums)
        n = len(nums)
        req_sum = ((n) * (n+1))//2
        
        return req_sum - list_sum