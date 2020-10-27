"""
see https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""
from collections import deque
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        chain = deque([(headID,0)])     # person, time spread to this person
        maxTime = 0
        # totalTime = 0

        md = {}
        for i in range(len(manager)):
            p = manager[i]
            if p in md:
                md[p] += i,
            else:
                md[p] = [i]

        while n:
            p, t = chain.popleft()
            t += informTime[p]          # time of this person got informed
            if p in md:
                for m in md[p]:
                    chain.append((m, t))
            maxTime = max(maxTime, t)
            n -= 1

        return maxTime

print(Solution().numOfMinutes(1, 0, [-1],[0]), 'should be 0')
print(Solution().numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]), 'should be 1')
print(Solution().numOfMinutes(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1]), 'should be 21')
print(Solution().numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]), 'should be 3')
print(Solution().numOfMinutes(4, 2, [3,3,-1,2], [0,0,162,914]), 'should be 1076')