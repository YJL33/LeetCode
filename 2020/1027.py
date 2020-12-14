"""
https://leetcode.com/problems/longest-arithmetic-subsequence/
"""
def longestArithSeqLength(self, A):
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                dp[j, A[j]-A[i]] = dp.get((i,A[j]-A[i]), 1) + 1
        return max(dp.values())

print(Solution().longestArithSeqLength([3,6,9,12]))
print(Solution().longestArithSeqLength([9,4,7,2,10]))
print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))