"""
https://leetcode.com/problems/daily-temperatures/
"""
import heapq
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # use heap
        # O(logn)*n
        h = []
        ans = [0 for _ in T]

        for i in range(len(T)):
            t = T[i]
            heapq.heappush(h, (t, i))
            while h and t > h[0][0]:
                tx, j = heapq.heappop(h)
                ans[j] = i-j

        return ans

print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

