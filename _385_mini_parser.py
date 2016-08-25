"""
385. Mini Parser

Given a nested list of integers represented as a string,
implement a parser to deserialize it.

Each element is either an integer,
or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

    String is non-empty.
    String does not contain white spaces.
    String contains only digits '0123456789[-,]'.

Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.

Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
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

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # Since the input is always well-formed
        # Use stack:
        # if '0123456789'   => update the number
        # if '['            => put in a NestedInteger() into stack
        # if ',' or ']'     => add the number into last element in stack
        #                   => pull out the last element in stack, if nothing left => return it
        # Time complexity: O(n)
        stack = []
        sigma, negmul = None, 1
        for c in s:
            if c == '-':
                negmul = -1
            elif '0' <= c <= '9':
                sigma = (sigma or 0) * 10 + int(c)
            elif c == '[':
                stack.append(NestedInteger())
            else:
                if sigma is not None:
                    stack[-1].add(NestedInteger(sigma * negmul))
                    sigma, negmul = None, 1
                if c == ']':
                    top = stack.pop()
                    if stack: stack[-1].add(top)
                    else: return top
        return NestedInteger((sigma or 0) * negmul)