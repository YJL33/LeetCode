"""
33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper_1(head, tail):
            # Find where pivot is
            while nums[head] > nums[tail]:
                mid = head + (tail-head)/2
                if nums[head] > nums[mid]:          # Pivot in the 1st half
                    tail = mid
                else:                               # Pivot in the 2nd half
                    head = mid + 1
            return head

        def helper_2(start, end):
            # Find target in sorted range
            while start < end:
                mp = start + (end-start)/2
                if nums[mp] == target:
                    return mp
                elif nums[mp] > target:         # target before mp
                    end = mp
                else:
                    start = mp+1
            if nums[start] == target:
                return start
            else:
                return -1

        L = len(nums)
        before_pivot = True

        if not nums: return -1
        if target < nums[0] and target > nums[-1]: return -1

        # with head and tail, we can know target is before pivot or after pivot
        if target < nums[0]: before_pivot = False

        # Find pivot
        pivot = helper_1(0, L-1)

        # Find target
        if before_pivot and pivot != 0:
            return helper_2(0, pivot-1)
        else:
            return helper_2(pivot, L-1)