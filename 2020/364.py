"""
364
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution:
    def __init__(self):
        self.arr = []
        self.maxDepth = 0
    def helper(self, nl, d):
        self.maxDepth = max(self.maxDepth, d)
        for x in nl:
            if x.isInteger():
                self.arr.append((x.getInteger(), d))
            else:
                self.helper(x.getList(), d+1)
        return
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.helper(nestedList, 1)
        print(self.arr, self.maxDepth)
        return sum([a*(self.maxDepth-b+1) for a,b in self.arr])
