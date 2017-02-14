"""
 169. Majority Element

    Total Accepted: 171811
    Total Submissions: 380757
    Difficulty: Easy
    Contributors: Admin

Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj, cnt = nums[0], 1

        for n in nums[1:]:
            if cnt == 0:
                maj, cnt = n, 1
            elif maj == n:
                cnt += 1
            else:
                cnt -= 1

        return maj
