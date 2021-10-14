# use DP
# dp[i] = the answer of numSquares while n == i
# dp[i] = min([dp[x]+1 for x in range(sqrt)])
# time analysis: O(n)

import collections
class Solution:
    def __init__(self):
        self.dp = collections.defaultdict(int)
        for i in range(1,4):
            self.dp[i] = i
        self.dp[0] = 0
        return
    def numSquares(self, n: int) -> int:
        if n <= 3: return self.dp[n]
        num = 4
        while num <= n:
            sqrt = int(pow(num, 0.5))
            tmp = [self.dp[num-i*i]+1 for i in range(1,sqrt+1)]
            self.dp[num] = min(tmp)
            num += 1
        return self.dp[n]

print(Solution().numSquares(4))
print(Solution().numSquares(5))
print(Solution().numSquares(6))
print(Solution().numSquares(7))
print(Solution().numSquares(8))