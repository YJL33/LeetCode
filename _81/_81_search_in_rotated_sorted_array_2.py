"""
81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def helper_1(head, tail):
            # Find where pivot is (where minimum value is)
            while head < tail:
                mid = head + (tail-head)/2
                if nums[tail] == nums[mid]:         # Moving tail is Legit, moving head is NOT
                    tail -= 1
                    if nums[tail] > nums[tail+1]:   # Don't miss the pivot
                        return tail+1
                elif nums[tail] > nums[mid]:        # Pivot in the 1st half
                    tail = mid
                else:                               # Pivot in the 2nd half
                    head = mid + 1
            return head

        def helper_2(start, end):
            # Find target in sorted range
            while start < end:
                mp = start + (end-start)/2
                if nums[mp] == target:
                    return True
                elif nums[mp] > target:         # target before mp
                    end = mp
                else:
                    start = mp+1
            if nums[start] == target:
                return True
            else:
                return False

        L = len(nums)
        before_pivot = True

        if not nums: return False
        if target < nums[0] and target > nums[-1]: return False

        # with head and tail, we can know target is before pivot or after pivot
        if target < nums[0]: before_pivot = False

        # Find pivot
        pivot = helper_1(0, L-1)

        # Find target
        if before_pivot and pivot != 0:
            return helper_2(0, pivot-1)
        else:
            return helper_2(pivot, L-1)