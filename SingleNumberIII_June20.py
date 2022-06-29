# problem link -> https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for i in counter.keys():
            if counter[i] == 1:
                ans.append(i)
                
        return ans