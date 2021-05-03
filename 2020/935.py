"""
935
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        # use DP
        if n == 0: return 0
        if n == 1: return 10

        dp = [1 for _ in range(10)]
        mp = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[3,9,0], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[2,4]}
        for i in range(2,n+1):
            tmp = [0 for _ in range(10)]
            for j in range(10):
                tmp[j] = sum([dp[p] for p in mp[j]])
            dp = tmp

        return sum(dp)%1000000007

print(Solution().knightDialer(1))
print(Solution().knightDialer(2))
print(Solution().knightDialer(3))
print(Solution().knightDialer(4))
print(Solution().knightDialer(3131))