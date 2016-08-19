"""
189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.

[show hint]
Hint:
Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # move last element to the front: 246ms
        k = k%len(nums)
        while k:
            nums.insert(0,nums.pop())
            k -= 1

    def rotate(self, nums, k):
        # move first element to the end: 156ms
        k = k%len(nums)
        while len(nums)-k:
            nums += nums.pop(0),
            k += 1

    def rotate(self, nums, k):
        # reverse method: 80ms (!!)
        k = k%len(nums)
        p = nums[-k-1::-1] + nums[:-k-1:-1]
        
        for i in xrange(len(p)):
            nums[i] = p[-i-1]