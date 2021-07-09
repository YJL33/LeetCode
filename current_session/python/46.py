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
            return [[n] for n in nums]
        res = []
        for i in range(len(nums)):
            tmp = self.permute([a for a in nums if a!=nums[i]])
            for t in tmp:
                res.append([nums[i]]+t)
        return res

print(Solution().permute([1,2,3,4]))
print(Solution().permute([1,2,3]))
print(Solution().permute([1]))
print(Solution().permute([]))
