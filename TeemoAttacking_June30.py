# problem link -> https://leetcode.com/problems/teemo-attacking/

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0

        for curr in range(len(timeSeries) - 1):
            if timeSeries[curr] + duration - 1 < timeSeries[curr + 1]:
                ans += duration
            else:
                ans += (timeSeries[curr+1] - timeSeries[curr])
        ans += duration
        return ans