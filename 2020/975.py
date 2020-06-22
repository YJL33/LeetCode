"""
975. Odd Even Jump

You are given an integer array A.

From some starting index, you can make a series of jumps.

The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps,
and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...),
you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.
If there are multiple such indexes j, you can only jump to the smallest such index j.

During even numbered jumps (ie. jumps 2, 4, 6, ...),
you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.
If there are multiple such indexes j, you can only jump to the smallest such index j.

(It may be the case that for some index i, there are no legal jumps.)

A starting index is good if, starting from that index,
you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.
"""
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        # find the index of the next smallest possible value for odd jump
        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        # find the index of the next biggest possible value for even jump
        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        # note that we can also solve this problem by using min/max heap
        # iterate from backward while maintaining the min/max heap so that we'll know whether the jump is possible or not

        # use DP
        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)