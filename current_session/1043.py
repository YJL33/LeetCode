"""
1043
"""
class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # initialization
        dp = [0 for x in range(len(A))]
        dp[0] = A[0]
        seenMax = A[0]
        for i in range(1,K):
            seenMax = max(seenMax, A[i])
            dp[i] = (i+1)*seenMax
        
        # find the maximum sum so far as if this is the end of a partition
        for j in range(K, len(A)):
            
            # go back K-1 steps to find the maximum so far
            seenMax = 0
            for back in range(K):
                seenMax = max(seenMax, A[j - back])
                prevSum = dp[j - back - 1]
                dp[j] = max(dp[j], prevSum + (back+1)*seenMax)
        
        return dp[-1]

print(Solution().maxSumAfterPartitioning(A = [1,15,7,9,2,5,10], K = 3))
print(Solution().maxSumAfterPartitioning(A = [1,4,1,5,7,3,6,1,9,9,3], K = 4))
print(Solution().maxSumAfterPartitioning(A = [1], K = 1))