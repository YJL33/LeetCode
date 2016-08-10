"""
229. Majority Element II

Given an integer array of size n,
find all elements that appear more than ⌊ n/3 ⌋ times.
The algorithm should run in linear time and in O(1) space.

Hint: How many majority elements could it possibly have?
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # implement Boyer-Moore Majority Vote Algorithm again
        # at most only 2 majority element
        # ++++++++
        # ++++++++
        # -------   (minority minus can not cancel out all majority)
        if not nums:
            return []

        if len(nums) == 1:
            return [nums[0]]

        m1 = m2 = 0.5
        c1 = c2 = 0

        for n in nums:              # here has 5 parallel situations
            if n == m1:             # c1 + 1
                c1 += 1
            elif n == m2:           # c2 + 1
                c2 += 1
            elif c1 == 0:           # assign new m1
                m1, c1 = n, 1
            elif c2 == 0:           # assign new m2
                m2, c2 = n, 1
            else:                   # c1 and c2 both - 1
                c1 -= 1
                c2 -= 1
            #print m1, m2

        if m1 != m2:
            return [x for x in [m1, m2] if nums.count(x) > len(nums)//3]
        else:
            if nums.count(m1) > len(nums)//3: return [m1]
            else: return []