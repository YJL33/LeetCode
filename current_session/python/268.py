from typing import List
class Solution:
    # clarification
    # are number sorted? if so, we can use binary search
    # if not we can use XOR or sum
    #
    # use sum
    # sum and check the diff
    # tc: O(n)
    # sc: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums)+1)]) - sum(nums)

    # use XOR
    # leverage x^x == 0, xor everything and see what's left
    # tc: O(n)
    # sc: O(1)
    def missingNumber_xor(self, nums: List[int]) -> int:
        xor = nums[0]
        for n in nums[1:]:
            xor ^= n
        for i in range(len(nums)+1):
            xor ^= i
        return xor

    # use binary search
    # [3,0,1,4,5,6]  -> [0,1,3,4,5,6] 
    #              index 0,1,2,3,4,5
    # find the first nums[i] s.t. nums[i] != i
    # tc: O(logn) for sorted, O(nlogn) for unsorted
    # sc: O(1)
    def missingNumber_bs(self, nums: List[int]) -> int:
        nums.sort()      
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > mid:            # good, seek to left hand side
                r = mid
            else:
                l = mid+1
        return l if nums[l] != l else l+1