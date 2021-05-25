"""
Sort Colors

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, numOfZeros, numOfTwos = 0, 0, 0

        for n in nums:
            if n == 0:
                numOfZeros += 1
            elif n == 2:
                numOfTwos += 1

        i, j = 0, len(nums)-1
        while numOfZeros:
            nums[i], i = 0, i+1
            numOfZeros -= 1
        while numOfTwos:
            nums[j], j = 2, j-1
            numOfTwos -= 1
        while i <= j:
            nums[i] = 1
            i += 1

        return

print Solution().sortColors([2,0,2,1,1,0])
print Solution().sortColors([2,0,1])
print Solution().sortColors([2,2,2,1,1,1,0,0,0])
print Solution().sortColors([1,1,1,1,1,1])
print Solution().sortColors([2,2,2,2,2,2,2])
print Solution().sortColors([1,2,0,1,2,0,1,2,0,1,2,0])