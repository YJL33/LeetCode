"""
31. Next Permutation

Implement next permutation,
which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Well, in fact the problem of next permutation has been studied long ago.
        # In the 14th century, Narayana Pandita gives the algorithm
        # (with minor modifications in notations to fit the problem statement):

        # 1. Find the largest index k such that nums[k] < nums[k + 1].
        #    If no such index exists, the permutation is sorted in descending order,
        #    just reverse it to ascending order and we are done.
        #    For example, the next permutation of [3, 2, 1] is [1, 2, 3].
        # 2. Find the largest index l greater than k such that nums[k] < nums[l].
        # 3. Swap the value of nums[k] with that of nums[l].
        # 4. Reverse the sequence from nums[k + 1] up to and including the final element nums[nums.size() - 1].

        if not nums: return

        l = len(nums)-1
        k = len(nums)-2

        while nums[k] >= nums[k+1] and k >= 0: k -= 1   # looking for k

        if k == -1:             # next permutation not exist, just return the 1st one
            nums.reverse()
        
        else:
            while nums[l] <= nums[k]: l -= 1            # looking for l
    
            #print k, l
            nums[k], nums[l] = nums[l], nums[k]         # swap the value of nums[k] and nums[l]
            
            i, j = k+1, len(nums)-1
            while i < j:                                # reverse the sequence from k+1 to the end
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
