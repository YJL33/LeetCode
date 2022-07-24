# simply simulate the process
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        leftEmpty = 0
        while numBottles:
            cnt += numBottles
            if leftEmpty > 0:
                numBottles += leftEmpty
            numBottles, leftEmpty = numBottles // numExchange, numBottles % numExchange
            # print("?", cnt, numBottles, leftEmpty)
                
        return cnt

# print(Solution().numWaterBottles(9,3))
print(Solution().numWaterBottles(15,8))
# print(Solution().numWaterBottles(5,5))
# print(Solution().numWaterBottles(2,3))
# print(Solution().numWaterBottles(12,3))

