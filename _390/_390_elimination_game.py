"""
390. Elimination Game

There is a list of sorted integers from 1 to n.
Starting from left to right,
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again,
but this time from right to left,
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again,
alternating left to right and right to left,
until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 10,
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
2 4 6 8 10 12 14 16
2 6 10 14
6 14
6

Output:
6
"""
class Solution(object):
    def lastRemaining(self, n):
        return self.helper(n)

    def helper(self, n, left=True):
        # recursion w/o using much memory
        if n <= 1:
            return 1
        if left:
            return 2*self.helper(n/2, False)
        else:
            if n&1:
                return 2*self.helper(n/2, True)
            else:
                return 2*self.helper(n/2, True)-1

    def lastRemaining3(self, n):
        # use flag
        # Memory Exceed Limit (L50)
        flag = [True]*n
        lvl, remain, start, end, left = 0, n, 0, n-1, True
        while remain > 1:
            if left:
                while not flag[start]: start += 1
                while not flag[end]: end -= 1
                flag[start:end+1:2**(lvl+1)] = [False]*len(xrange(start,end+1,2**(lvl+1)))
            else:
                while not flag[start]: start += 1
                while not flag[end]: end -= 1
                flag[end:start-1:-(2**(lvl+1))] = [False]*len(xrange(end,start-1,-(2**(lvl+1))))
            lvl, remain, left = lvl+1, remain/2, not left

        for i in xrange(start, end+1):
            if flag[i]:
                return i+1

    def lastRemaining2(self, n):
        # implement iterative version
        # Memory Exceed Limit (70)
        res = range(1,n+1)
        left = True
        while len(res) > 1:
            if left:
                res = res[1::2]
            else:
                res = res[-2::-2][::-1]
            left = not left

        return res[0]

    def lastRemaining1(self, n):
        # implement recursion (no need to check n <= 0)
        # Memory Exceed Limit (L84)
        return self.helper1(range(1,n+1))

    def helper1(self, res, left=True):
        #print "\nhelper: ", res
        if len(res) == 1: return res[0]
        if left:
            res = res[1::2]
            return self.helper1(res, not left)
        else:
            res = res[-2::-2][::-1]
            return self.helper1(res, not left)
