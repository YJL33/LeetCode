"""
416
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2: return False
        nums = sorted(nums, reverse=True)
        target = int(sum(nums)/2)
        seenSum = set()

        for i in range(len(nums)):
            if nums[i] > target:
                return False
            if nums[i] == target or target-nums[i] in seenSum:
                return True
            elif not seenSum:
                seenSum.add(nums[i])
            else:
                toAdd = set()
                for x in seenSum:
                    newSum = x+nums[i]
                    if newSum < target and newSum not in seenSum: toAdd.add(newSum)
                seenSum = seenSum.union(toAdd)
        return False

print(Solution().canPartition([1,5,11,5]))
print(Solution().canPartition([1,2,3,5]))