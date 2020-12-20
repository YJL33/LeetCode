"""
see https://leetcode.com/problems/permutations/
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            tmp = self.permute(nums[:i]+nums[i+1:])
            for t in tmp:
                ans.append([nums[i]]+t)
        return ans

print(Solution().permute([1,2,3,4]))
print(Solution().permute([1,2,3]))
print(Solution().permute([1]))
print(Solution().permute([]))
