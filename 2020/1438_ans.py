"""
see https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""
class Solution(object):
    def longestSubarray(self, A, limit):
        maxd = collections.deque()
        mind = collections.deque()
        i = 0
        for a in A:
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()
            maxd.append(a)
            mind.append(a)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                i += 1
        return len(A) - i


print(Solution().longestSubarray([10,1,2,4,7,2],5))
print(Solution().longestSubarray([8,2,4,7],4))
print(Solution().longestSubarray([8],10))
print(Solution().longestSubarray([10,1,2,4,7,2],5))
print(Solution().longestSubarray([4,2,2,2,4,4,2,2],0) == 3)
print(Solution().longestSubarray([4,8,5,1,7,9],6) == 3)

