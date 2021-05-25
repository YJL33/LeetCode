"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            n = abs(nums[i])
            # print(i,n)
            if nums[n-1] < 0:
                ans += n,
            else:
                nums[n-1] = (-1)*nums[n-1]
        return ans

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
print(Solution().findDuplicates([1,2,3,4,5,6,6,8]))
print(Solution().findDuplicates([2,2]))
