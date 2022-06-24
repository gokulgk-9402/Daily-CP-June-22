# problem link -> https://leetcode.com/problems/construct-target-array-with-multiple-sums/submissions/

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        maxheap = []
        for number in target:
            heappush(maxheap, -number)
        total = sum(target)

        while maxheap:
            top = -maxheap[0]
            diff = total-top
            heappop(maxheap)
            total = total - top
            if diff == 1 or top == 1:
                return True
            if diff > top or diff == 0 or top%diff == 0:
                return False

            heappush(maxheap, -(top%diff))
            total += top%diff

        return False