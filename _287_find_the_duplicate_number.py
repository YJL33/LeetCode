"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        try:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow is not fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            # Here slow = fast = meeting point (M)
            # Use two pointers each begin at head and M, they will meet at entry.
            # print "fast", fast, "slow", slow
            entry = 0
            while slow is not entry:
                slow = nums[slow]
                entry = nums[entry]
            return entry
        except:
            return None

# This solution failed on 1 test sample, which has correct output in local environment.