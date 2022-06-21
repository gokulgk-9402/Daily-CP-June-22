class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = 0
        b = 0
        merged = []
        
        while len(merged) < ((len(nums1)+ len(nums2))//2 +1):
            if a >= len(nums1):
                merged.append(nums2[b])
                b += 1
            elif b >= len(nums2):
                merged.append(nums1[a])
                a += 1
            elif nums1[a] < nums2[b]:
                merged.append(nums1[a])
                a += 1
            else:
                merged.append(nums2[b])
                b += 1
        
        if (len(nums1) + len(nums2)) %2:
            return merged[-1]
        else:
            return (merged[-1] + merged[-2])/2