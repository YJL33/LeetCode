"""
https://leetcode.com/problems/course-schedule-ii/
"""
import collections
class Solution(object):
    def __init__(self):
        self.cd = collections.defaultdict(list)
        self.visited = []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # use dfs
        for a,b in prerequisites:
            self.cd[a].append(b)

        self.visited = [0 for _ in range(numCourses)]

        res = []
        for i in range(numCourses):
            if self.dfs(i, res):
                return []
        return res

    def dfs(self, x, res):
        # print x, self.visited
        # return True if there's a loop
        if self.visited[x] == -1:
            return False
        if self.visited[x] == 1:
            return True
        self.visited[x] = 1
        for pre in self.cd[x]:
            if self.dfs(pre, res):
                return True
        self.visited[x] = -1
        res.append(x)
        return False
        

print(Solution().findOrder(numCourses = 2, prerequisites = [[1,0]]))
print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(numCourses = 2, prerequisites = [[1,0]]))

a = Solution()
print(a.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(a.visited)
print(a.__vs)