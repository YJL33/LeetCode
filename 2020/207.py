"""
207
"""
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # courses: 0 to numCourses-1
        # detect whether there's a loop

        preD = collections.defaultdict(list)    # key: class, value: preRequisite
        for p in prerequisites:
            a, b = p[0], p[1]
            preD[a].append(b)

        visit = [0 for _ in range(numCourses)]

        # detect whether x is in a loop or not
        def detectLoop(x):
            visit[x] = 1                # mark here while checking the loop
            if x in preD:               # there's a preRequisite
                for pre in preD[x]:
                    tmp = False             # no Loop
                    if visit[pre] == 0:     # need to check its preRequisite
                        tmp = detectLoop(pre)
                    elif visit[pre] == 1:   # there's a loop!
                        return True
                    else:                   # -1
                        continue
                    if tmp:
                        return True
            visit[x] = -1               # no loop here
            return False                
        
        for i in range(numCourses):
            if detectLoop(i):
                return False
        return True

print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(2, [[1,0], [0,1]]))
print(Solution().canFinish(3, [[1,0], [2,1], [0,2]]))