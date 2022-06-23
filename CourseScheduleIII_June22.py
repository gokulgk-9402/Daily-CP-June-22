# problem link -> https://leetcode.com/problems/course-schedule-iii/

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        time = 0
        heap = []
        for course in sorted(courses, key=lambda x: x[1]):
            if course[0] <= course[1]:
                if course[0] + time <= course[1]:
                    heapq.heappush(heap, -course[0])
                    time += course[0]
                else:
                    if heap[0] < -1 * course[0]:
                        time += heapq.heappop(heap)
                        time += course[0]
                        heapq.heappush(heap, -1 * course[0])

        return len(heap)