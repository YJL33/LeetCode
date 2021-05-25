"""
31. Next Permutation

Implement next permutation,
which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible,
it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

Accepted
364,426
Submissions
1,127,442
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return

        # find k: the largest index k such that nums[k] < nums[k + 1]
        k = len(nums)-2
        while nums[k] >= nums[k+1] and k >= 0:
            k -= 1

        if k == -1:
            # nums.reverse()
            return nums[::-1]

        else:
            l = len(nums)-1
            while nums[l] <= nums[k]:
                l -= 1
            # print "k: ", k
            # print "l: ", l 
            nums[l], nums[k] = nums[k], nums[l]
            i, j = k+1, len(nums)-1
            # print "before: ", nums, i, j
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1

            return nums


print Solution().nextPermutation([3,2,1])
print Solution().nextPermutation([1,3,2])
print Solution().nextPermutation([1,1,5])
print Solution().nextPermutation([6,5,4,3,2,1])
print Solution().nextPermutation([4,5,6,3,2,1])