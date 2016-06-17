"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

For example:

2, [[1,0]]

There are a total of 2 courses to take.
To take course 1 you should have finished course 0.     (latter one is prerequisite)
So it is possible.

2, [[1,0],[0,1]]

There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1.
So it is NOT possible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.

Hints:
This problem is equivalent to finding if a cycle exists in a directed graph.
If a cycle exists, no topological ordering exists so it will be impossible to take all courses.
Topological Sort can be done via DFS
Topological sort could also be done via BFS.

"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # since the courses are numbered from 0 to n-1,
        # we can use an array instead of a dictionary to storage pre-requisites of each classes

        course_array = [[] for i in xrange(numCourses)] # each sub-list records the pre-requisites
        visit = [0 for i in xrange(numCourses)]         # check whether these is a loop
        for edge in prerequisites:
            course_array[edge[0]].append(edge[1])

        def dfs(x):
            """
            find whether there's a loop or not
            """
            if visit[x] == -1:          # visit here earlier, there's no loop.
                return False
            if visit[x] == 1:           # there's a loop!
                return True

            visit[x] = 1                # begin to check this node and its prerequisite
            for v in course_array[x]:
                if dfs(v):
                    return True
            visit[x] = -1
            return False

        for i in xrange(numCourses):
            if dfs(i):
                return False            # if there's a loop => NOT possible to complete.
        return True                     # vice versa



