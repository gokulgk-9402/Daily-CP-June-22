# problem link -> https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
# this is kind of brute force approach, there's more efficient approach that runs in O(n)