# problem link -> https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return 0

        diff_array = [nums[i] - nums[i-1] for i in range(1, length)]

        curr = 0
        total = 0

        for i in range(1, length - 1):
            if diff_array[i]!=diff_array[i-1]:
                if i - curr > 1:
                    total+= (((i-curr)*(i-curr-1))/2)
                curr = i

            if i == length-2 and i-curr >= 1:
                total += (((i-curr+1)*(i-curr))/2)

        return int(total)