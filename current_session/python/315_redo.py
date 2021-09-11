# analysis:
# brute force: O(n^2)
#
# heap 
# maintain 2 heaps, min heap H1 and max heap H2
# where all a in H1 > nums[i] and all b in H2 < nums[i]
# simply store the size of H2 while propagating the whole arrays
# O(n * (logn + x)), where x is the moves needed to adjust both heap,
# x will near n if the heap is too big
# 
# binary search
# use an array to replace 2 heaps above, and maintain the array as sorted
# use binary search to find the index
# we need a data structure that has insert = O(1), s.t.
# overall: O(n* (logn + 1))
# 
# merge Sort
# split, if any element crossed (from right to left while merging), i+=1
# O(n*logn)

# use merge sort
from typing import List
import heapq
class Solution:
    def countSmaller(self, nums):
        def sort(enum):
            if not enum: return
            half = len(enum) // 2
            if half:
                # print('half:', half)
                l, r = enum[:int(half)], enum[int(half):]
                left, right = sort(l), sort(r)
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    # use heap
    def countSmaller_TLE(self, nums:List[int]) -> List[int]:
        minH, maxH = [nums[-1]], []
        res = [0]*len(nums)
        for i in range(1,len(nums)):
            n = nums[~i]

            # append n into heap, and adjust the size
            minH, maxH = self.adjustHeap(minH, maxH, n)
            res[~i] = len(maxH)

            heapq.heappush(minH, n)
    
        return res
    
    def adjustHeap(self, minH, maxH, target):
        # print('befor:', minH, maxH)
        while minH and minH[0] < target:
            x = heapq.heappop(minH)
            heapq.heappush(maxH, -1*x)
        
        while maxH and -1*maxH[0] >= target:
            x = heapq.heappop(maxH)
            heapq.heappush(minH, -1*x)

        # print('after:', minH, maxH)
        return minH, maxH

print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmaller([1,1,1]))
print(Solution().countSmaller([1]))
print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]))
print(Solution().countSmaller([1,2,3,4,5,6,7,8,9]))