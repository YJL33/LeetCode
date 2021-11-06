class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row-1
        
print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))