"""
https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List
class Solution(object):
    # clarifications:
    # any restrictions on time/space? (e.g. timeout/memory)
    # duplicate occurance? (more than 2 times)
    
    # naive approach: count
    # create an array (or a set) which is a counter for arr[i]
    # go through the whole array and see if anything duplcated
    # tc: O(N)
    # sc: O(N), (use bit manipulation here -> O(1), does that count?)
    # sys.getsizeof(1<<10000) = 13360 bytes
    
    # binary sesarch approach:
    # range from 1 to max(nums), which is n
    # for each m (guess), go through the whole array to count how many numbers are smaller than m
    # if count >= m: duplicate is smaller than m or equal to m
    # else: duplicate is bigger than m
    # e.g. [1,2,2,3,4,5,6,7]
    # binary search, m = 4, count(4) = 5, at the left side
    # binary search, m = 2, count(2) = 3, at the left side
    # binary search, m = 1, count(1) = 1, at the right side, note that we don't care count(x) == x
    # now l == r == 2
    # in other word, we're looking for smallest x s.t. count(x) > x
    # tc: O(NlogN), because we need to go through the whole array everytime
    # sc: O(1)
    def findDuplicate_bsearch(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        while l < r:
            m = (r+l)//2
            count = sum([1 if (n <= m) else 0 for n in nums])
            if count > m:
                r = m                           # we want it, r=m
            else:
                l = m+1                         # we don't want it, l=m+1
        return l

    # tortoise-hare algorithm
    # treat this as a graph
    # each node is pointing to its next node
    # e.g. [1,3,2,2]
    # node 0 next 1, node 1 next 3, node 3 next 2, node 2 next 2
    # if there's a loop(duplicate), then fast/slow pointer will meet somewhere
    # tc: O(N)
    # sc: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]
        while True:
            fast, slow = nums[nums[fast]], nums[slow]
            if fast == slow:
                break
        
        # now they met, start from head again
        slow = nums[0]
        while fast != slow:
            fast, slow = nums[fast], nums[slow]
        
        # now they met again, which is at the duplicate point
        return fast