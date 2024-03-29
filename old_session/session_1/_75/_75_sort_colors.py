"""
75. Sort Colors

Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0

        while i+j < len(nums):
            n = nums[i]
            if nums[i] == 1:
                i += 1              # count of un-treated colors
            elif nums[i] < 1:
                nums.insert(0, n)
                nums.pop(i+1)
                i += 1              # count of colors we put in front of array
            elif nums[i] > 1:
                nums += n,
                nums.pop(i)
                j += 1              # count of colors we put in the end of array

        return