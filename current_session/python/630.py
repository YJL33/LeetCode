from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # naive thoughts:
        # (similar to LIS, either use binary search or DP)
        # DP:
        # keep update:
        # a) the local max (for each course[i], find the maximum number of courses ending with course[i])
        # b) the global max
        heap, time = [], 0
        for t, end in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(heap, -t)
            if time > end:
                nt = heapq.heappop(heap)
                time += nt
        return len(heap)