"""
 442. Find All Duplicates in an Array

    Total Accepted: 6444
    Total Submissions: 14237
    Difficulty: Medium
    Contributors: shen5630

Given an array of integers, 1 ≦ a[i] ≦ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:                  # change n into index
            if nums[abs(n)-1] > 0:      # if positive: never visit before, change it into negative
                nums[abs(n)-1] *= (-1)
            else:                       # if negative: this n is duplicate
                ans += abs(n),
        return ans