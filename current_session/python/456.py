from typing import List
import sortedcontainers

# any duplicates?
# length of nums?
# upper/lowerbound of nums[i]?
#
class Solution:
    # use stack
    # similar to sortlist solution
    # keep an min_array for the min value for each element
    # note that the min value should not include itself.
    #
    # stack keeps everything at right hand side
    # for element i, if we see anything smaller than min_value[i], throw it away (pop it out of stack)
    #
    # tc: O(n)
    # sc: O(stack)
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_array = [-1] * len(nums)
        min_array[0] = nums[0]
        for i in range(1, len(nums)):
            min_array[i] = min(min_array[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= min_array[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False
        
    # use sortedlist
    # scan from left to right, keep update the min value we seen at the left-hand side
    # scan from right to left, maintain a sorted list for each element at the right-hand side
    # and search if there's any pattern match
    # tc:
    # O(n) to find all minimal values at the left-hand side
    # O(LlogL), where L is the length of sortedList, worst case O(nlogn)
    # overall O(n)+O(nlogn)
    # sc:
    # O(n) to store all minimal values at the left-hand side
    # O(L), where L is the length of sortedlist, worst case O(n)
    def find132pattern_sortedlist(self, nums: List[int]) -> bool:
        left_min = [nums[0]]
        for n in nums[1:]:
            left_min.append(min(n, left_min[-1]))
        
        sl = sortedcontainers.SortedList([nums[-1]])
        for i in range(len(nums)-2, -1, -1):
            one = left_min[i]
            three = nums[i]
            idx = sl.bisect_right(one)
            if idx < len(sl):
                two = sl[idx]
                if one < two < three:
                    return True
            sl.add(three)
        
        return False