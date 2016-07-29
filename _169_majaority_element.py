"""
169. Majority Element

Given an array of size n,
find the majority element.

The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Majority Vote Algorithm
        # http://www.cs.utexas.edu/~moore/best-ideas/mjrty/

        # If use a dictionary and a threshold float(len(nums))/2,
        # can do the same thing and even for >= n/2

        majority = nums[0]
        count = 1

        for n in nums[1:]:
            if count == 0:
                count += 1
                majority = n
            elif majority == n:
                count += 1
            else:
                count -= 1

        return majority
