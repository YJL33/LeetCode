from typing import List
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 1. pick x > 1, remove x stones
        # 2. add sum of removed stones
        # 3. place a new one, val == sum of removed stones
        # score diff: alice's score - bob's score
        # alice: maximize the score diff
        # bob: minimize the score diff

        # use DP
        # use prefix sum
        prefix = [stones[0]]
        for s in stones[1:]:
            prefix.append(prefix[-1]+s)

        # print('prefix', prefix)

        max_diff = prefix[-1]
        for i in range(len(prefix)-2, 0, -1):
            v = prefix[i]
            max_diff = max(max_diff, v-max_diff)
        return max_diff

print(Solution().stoneGameVIII([-1,2,-3,4,-5]), '== 5')
print(Solution().stoneGameVIII([7,-6,5,10,5,-2,-6]), '== 13')
print(Solution().stoneGameVIII([-10,-12]), '== -22')
print(Solution().stoneGameVIII([-39,-23,-43,-7,25,-36,-32,17,-42,-5,-11]), '== 11')
