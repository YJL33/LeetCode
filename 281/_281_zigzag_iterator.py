"""
 281. Zigzag Iterator

    Total Accepted: 19450
    Total Submissions: 40595
    Difficulty: Medium
    Contributors: Admin

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]

By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".
For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]

It should return [1,4,8,2,5,9,3,6,7].
"""
import itertools
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        def vals():
            for i in itertools.count():
                for v in v1, v2:
                    if i < len(v):
                        yield v[i]
        self.vals = vals()
        self.n = len(v1) + len(v2)

    def next(self):
        """
        :rtype: int
        """
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.n > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())