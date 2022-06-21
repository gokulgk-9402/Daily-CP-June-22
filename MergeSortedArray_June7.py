# problem link -> https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        temp = nums1[:m]
        
        while i+j < m +n:
            if i >= m:
                nums1[i+j] = nums2[j]
                j += 1
            elif j >= n:
                nums1[i+j] = temp[i]
                i += 1
            elif temp[i] <= nums2[j]:
                nums1[i+j] = temp[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1