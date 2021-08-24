# use dfs
# create the prerequisite map
# use dfs
from typing import List
import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites:List[List[int]]) -> List[int]:
        pd = collections.defaultdict(list)
        for a,b in prerequisites:
            pd[a].append(b)           # complete b->a
        
        self.visited = set()
        self.res = []
        self.loopFlag = False

        def dfs(a):
            self.visited.add(a)
            if a in pd:
                for b in pd[a]:
                    if b not in self.visited:
                        dfs(b)
                    elif b not in self.res:
                        self.loopFlag = True
            self.res.append(a)
            return
        
        for n in range(numCourses):
            if n not in self.visited:
                dfs(n)
        
        return [] if self.loopFlag else self.res