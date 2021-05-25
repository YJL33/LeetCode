"""
https://leetcode.com/problems/task-scheduler/
"""
import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # math
        # ["A","A","A","B","B","B"], n = 2
        # A -> B -> idle -> A -> B -> idle -> A -> B
        # A and B both has maxCount=3
        # observe that in "one round", there's (n+1) in the round
        # in the last round, only elements has the maxCount are in the round
        # we got: (n+1)*(maxCount-1)+numOfElementsHasMaxCount

        taskCnt = collections.defaultdict(int)
        maxSeen = 0
        for t in tasks:
            taskCnt[t] += 1
            if taskCnt[t] >= maxSeen:
                maxSeen = taskCnt[t]

        maxCnt = 0
        for k, v in taskCnt.items():
            if taskCnt[k] == maxSeen:
                maxCnt += 1

        ans = (n+1)*(maxSeen-1)+maxCnt
        return max(len(tasks),ans)      # in case maxSeen = 1
