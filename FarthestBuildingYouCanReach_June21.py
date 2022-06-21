# problem link -> https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        min_heap = []
        total = len(heights)

        for i in range(total - 1):
            to_climb = heights[i+1] - heights[i]

            if to_climb <= 0:
                continue

            heapq.heappush(min_heap, to_climb)

            if len(min_heap) > ladders:
                bricks_needed = heapq.heappop(min_heap)
                bricks -= bricks_needed

            if bricks < 0:
                return i

        return total - 1
