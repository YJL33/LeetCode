from typing import List
class Solution:
    def findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        # brute force:
        # sort and then compare sorted and unsorted array
        # tc: O(nlogn) sort + O(n) compare
        # sc: O(n) to store sorted array
        arr = [n for n in nums]
        arr.sort()
        
        i, j = 0, len(nums)-1
        while i < len(nums) and nums[i] == arr[i]:
            i += 1
        while j >= 0 and nums[j] == arr[j]:
            j -= 1
        
        return max(j+1-i, 0)

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # optimization
        # find the smallest/biggest element at incorrect place
        # e.g. [2,6,4,8,10,9,15]
        # biggest element at incorrect place is 10, which should locate at i=5
        # smallest element at incorrect place is 4, which should locate at i=1
        # edge case: [1,2,3,3,3]
        #
        # tc: O(n)
        # sc: O(1)
        if len(nums) == 1: return 0
        prev_big, right = 0, 0
        for i in range(1,len(nums)):
            if nums[i] >= nums[prev_big]:
                prev_big = i
            else:
                right = i
        prev_small, left = len(nums)-1, len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= nums[prev_small]:
                prev_small = i
            else:
                left = i
        # print('nums, right, left', nums, right, left)
        return max(right+1-left, 0)
            
