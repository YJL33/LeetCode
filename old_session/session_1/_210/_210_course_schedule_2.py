"""
210. Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]

There are a total of 2 courses to take.
To take course 1 you should have finished course 0.
So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]

There are a total of 4 courses to take.
To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices.
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course_array = [[] for i in xrange(numCourses)] # each sub-list records the pre-requisites
        visit = [0 for i in xrange(numCourses)]         # check whether these is a loop
        res = []                                        # THE course ordering
        for edge in prerequisites:
            course_array[edge[0]].append(edge[1])

        # FIRST, put courses that don't need prerequisites into ordering.
        i = 0
        while i < numCourses:
            if len(course_array[i]) == 0:
                res += i,               # add into ordering.
                visit[i] = -1           # visited.
            i += 1

        def dfs(x, res):
            """
            find whether there's a loop or not
            """
            if visit[x] == -1:          # visit here earlier, there's no loop.
                return False
            if visit[x] == 1:           # there's a loop!
                return True

            visit[x] = 1                # begin to check this node and its prerequisite
            for v in course_array[x]:
                if dfs(v, res):
                    return True
            visit[x] = -1               # check PASSED, add this course into ordering. 
            res.append(x)               # Here prerequisite will be added earlier.
            return False

        # begin from the root
        for i in xrange(numCourses):
            if dfs(i, res):
                return []           # if there's a loop => NOT possible to complete.
        
        return res




