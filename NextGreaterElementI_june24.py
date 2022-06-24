# problem link -> https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {}
        result = []
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                ans[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            result.append(ans.get(num, -1))

        return result