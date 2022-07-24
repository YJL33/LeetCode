"""
see https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
from typing import List
class Solution(object):
        # brute force: check each pair of l, r
        # time: O(n3)

        # leverage monotonic increasing stack:
        # use it to find the previous smaller element and next smaller element for any h[i] in h
        #
        # go through all h in heights, and add all of them into stack
        # while adding, if the height is increasing (e.g., [3,4,5]), keep add them into stack
        # if decreasing, then update the answer by popping out previous h in stack
        #
        # e.g. [3,4,1]
        # we have 1 < 3: 
        # pop 4, ans = max(3, 1*4) = 4
        # pop 3, ans = max(4, 2*3) = 6
        # so on and so forth
        # time: O(n)

        # most skillful part: add 0 at the end of heights
        # check unit test L47, we'll find that answer is only calculated until we reach the end
    def largestRectangleArea(self, A: List[int]) -> int:
        st = [len(A)]
        A += 0,
        ans = 0
        for i in range(len(A)):
            while A[i] < A[st[-1]]:
                H = A[st.pop()]
                W = i-st[-1]-1
                ans = max(ans, H*W)
            stack += i,
        return ans


print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([1,2,3,4,5,6,7]))