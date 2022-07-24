from sortedcontainers import SortedList
from typing import List
class Solution:
    # clarification:
    # upperbound/lowerbound of nums[i]?
    # upperbound/lowerbound of length of nums?
    # any restrictions on memory or timeout?
    # 0 <= i < j < len(nums), nums[i] > 2*nums[j]
    # is the array sorted?
    #
    # thoughts
    # mergesort
    # while merging, count how many (i,j) s.t. nums[i] > 2*nums[j]
    # tc: O(nlogn)
    # sc: O(n)
    #
    # sortedlist
    # use sortedlist, from right to left, for each i, binary search each j s.t. nums[i] > 2*nums[j]
    # tc: O(nlogn)
    # sc: O(n)
    #
    # dummy cases
    # e.g. [1,3,2,3,1]
    #
    # choose sortedlist (cleaner)
    def reversePairs(self, nums: List[int]) -> int:
        arr = SortedList()
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if len(arr) != 0:
                count += arr.bisect_left(nums[i])
            arr.add(2*nums[i])
        return count
            
    def reversePairs_ms(self, nums):
        