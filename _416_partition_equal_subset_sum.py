"""
416. Partition Equal Subset Sum

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that:
the sum of elements in both subsets is equal.

Note:
Both the array size and each of the array element will not exceed 100.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(start, path, target):
            if target < 0: return
            elif target == 0: return True
            for i in xrange(start, len(nums)):
                if helper(i+1, [nums[i]]+path, target-nums[i]):
                    return True
            return False

        return False if sum(nums)%2 else helper(0, [], sum(nums)/2)