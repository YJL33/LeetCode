"""
698
"""
import collections
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # handle edge cases
        if k == 1:
            return True
        if k == len(nums):
            return len(set(nums)) == 1
        
        # calculate avg and sort
        nSum = sum(nums)
        tgt = nSum/k

        nums.sort()
        if nums[-1] > tgt: return False

        while nums[-1] == tgt:
            k -= 1
            nums.pop()
        
        nums = nums[::-1]
        sums = [0]*k

        def dfs(i):
            if i == len(nums):
                return len(set(sums)) == 1
            for j in range(k):
                sums[j] += nums[i]
                if sums[j] <= tgt and dfs(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0:
                    break
            return False

        return dfs(0)
        

print(Solution().canPartitionKSubsets(nums = [1,2,3,4], k = 3))
print(Solution().canPartitionKSubsets(nums = [4,3,2,3,5,2,1], k = 4))
print(Solution().canPartitionKSubsets(nums = [2,2,3,3,4], k = 2))
print(Solution().canPartitionKSubsets(nums = [1,1,1,1,1,1,1,2,2,3,3,4], k = 3))
print(Solution().canPartitionKSubsets([2,2,2,2,3,4,5],4))
print(Solution().canPartitionKSubsets([1,1,1,1,2,2,2,2],2))

