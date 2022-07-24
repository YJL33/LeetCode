class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        self.memo = {}
        return self.helper([x for x in range(1, maxChoosableInteger + 1)], desiredTotal)

    def helper(self, nums, desiredTotal):      
        h = tuple(nums)
        if h in self.memo:
            return self.memo[h]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[h]= True
                return True
        self.memo[h] = False
        return False
