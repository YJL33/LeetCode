"""
421. Maximum XOR of Two Numbers in an Array

    Total Accepted: 61
    Total Submissions: 417
    Difficulty: Medium
    Contributors: Admin

Given a list of numbers, a[0], a[1], a[2], … , a[N-1],
where 0 <= a[i] < 2^32. Find the maximum result of a[i] XOR a[j].

Could you do this in O(n) runtime?

Input: [3, 10, 5, 25, 2, 8]
Output: 28
"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)