# problem link -> https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # this is a more efficient approach using hashmap
        hashmap = {}
        for index1, value1 in enumerate(nums):
            value2 = target - value1
            if (index2:= hashmap.get(value2)) is not None:
                return [index1, index2]
            else:
                hashmap[value1] = index1