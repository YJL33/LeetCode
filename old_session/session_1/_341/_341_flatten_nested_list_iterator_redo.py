"""
 341. Flatten Nested List Iterator

    Total Accepted: 23847
    Total Submissions: 62536
    Difficulty: Medium
    Contributors: Admin

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,4,6].
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Use stack
        self.stack = [[nestedList, 0]]      # the next one is '0th' of this list

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            nl, i = self.stack[-1]
            self.stack[-1][1] += 1
            return nl[i].getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            nl, i = self.stack[-1]
            if i == len(nl):
                self.stack.pop()            # this list is ended, pop and check next position.
            else:
                x = nl[i]
                if x.isInteger():           # next integer is this element.
                    return True
                else:                       # next integer in this sublist.
                    self.stack[-1][1] += 1
                    self.stack += [x.getList(), 0],      # put the sublist into stack
        return False
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())