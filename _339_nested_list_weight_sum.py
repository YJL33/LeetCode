"""
339. Nested List Weight Sum

    Total Accepted: 9476
    Total Submissions: 16084
    Difficulty: Easy

Given a nested list of integers,
return the sum of all integers in the list weighted by their depth.

Each element is either an integer,
or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27.
(one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList, layer=1):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # recursive
        if not nestedList: return 0
        wsum = 0
        for n in nestedList:
            if n.isInteger():
                wsum += layer*n.getInteger()
            else:
                for i in n.getList():
                    wsum += self.depthSum([i], layer+1)
        return wsum

        # iterative
    def depthSum(self, nestedList):
        if len(nestedList) == 0: return 0
        stack, wsum = [], 0
        
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            nestint, depth = stack.pop(0)
            if nestint.isInteger():
               wsum += depth * nestint.getInteger()
            else:
                for i in nestint.getList():
                    stack.append((i,depth+1))
        return wsum