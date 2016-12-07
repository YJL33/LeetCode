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
        self.dct = {}
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # apply mergesort
        if not nums: return []
        # nums = self.rptfixer(nums)
        self.dct, copy, ans = {}, [], []
        for n in nums:
            self.dct[n] = 0
            copy += n,
        
        # assert len(nums) == len(self.dct)
        print self.msort(0, copy)
        for n in nums:
            ans += self.dct[n],
        return ans

    def rptfixer(self, nums):
        dct, strnums = {}, ["" for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            if nums[i] not in dct: dct[nums[i]] = [i]
            else: dct[nums[i]] += i,
        for k in dct:
            if len(dct[k]) > 1:
                cnt = 0
                while cnt < len(dct[k]):
                    strnums[dct[k][cnt]] = str(k)+chr(cnt+97)
                    cnt += 1
            else:
                strnums[dct[k][0]] = str(k)+chr(95)
        # print strnums, nums
        return strnums

    def msort(self, h, lst):                # h: beginning index of list
        # merge sort body
        L = len(lst)
        if L == 1:                          # base case
            return lst
        else:                               # recursive case, pass the original index to merger
            return self.merger(h, self.msort(h, lst[:int(L/2)]), self.msort(h+int(L/2), lst[int(L/2):]))

    def merger(self, s, l, r):
        # merger
        new, curl, curr = [], 0, 0
        # print l, r
        while curl < len(l) and curr < len(r):
            if l[curl] <= r[curr]:
                new += l[curl],
                curl += 1
            else:
                for e in l[curl:]: self.dct[e] += 1         # COUNT INVERSIONS HERE
                # print self.dct
                new += r[curr],
                curr += 1
        if curl < len(l):
            new += l[curl:]
            # print('+', len(l)-curl)
        if curr < len(r):
            new += r[curr:]
        return new
