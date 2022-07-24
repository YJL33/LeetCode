from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # find the minimal diff of 2 groups of partial sum
        # (knapsack problem)
        dp = {0}
        sumA = sum(stones)
        for a in stones:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)