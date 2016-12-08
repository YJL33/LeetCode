"""
315. Count of Smaller Numbers After Self

    Total Accepted: 23154
    Total Submissions: 69558
    Difficulty: Hard
    Contributors: Admin

You are given an integer array nums and you have to return a new counts array.

The counts array has the property:
counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""

class Solution(object):
    def __init__(self):
        self.ans = []

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # apply mergesort (refer to inversion.py), 2 issues:
        self.ans = [0 for n in nums]
        self.msort([n for n in enumerate(nums)])            # 1. use enumerate to fix repeat
        return self.ans

    def msort(self, enum):
        # merge sort body
        if len(enum) > 1:
            left, right = self.msort(enum[:(len(enum)/2)]), self.msort(enum[(len(enum)/2):])
            enum, cl, cr = [], 0, 0
            while cl < len(left) or cr < len(right):
                if cr == len(right) or (cl < len(left) and left[cl][1] <= right[cr][1]):
                    self.ans[left[cl][0]] += cr                 # 2. GOTTA COUNT HERE
                    enum += left[cl],
                    cl += 1
                else:
                    # for e in left[cl:]: self.ans[e[0]] += 1   # IF COUNT INVERSIONS HERE => TLE
                    enum += right[cr],
                    cr += 1
        return enum