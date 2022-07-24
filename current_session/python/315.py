"""
see https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
# clarification:
# any restrictions on time/space?
# upper/lower bound of nums[i]: -10000 <= nums[i] <= 10000
# upper/lower bound of len(nums): 1 <= nums.length <= 100000
# 
# brute force: O(n^2)
#
# heap 
# maintain 2 heaps, min heap H1 and max heap H2
# where all a in H1 > nums[i] and all b in H2 < nums[i]
# simply store the size of H2 while propagating the whole arrays
# O(n * (x * logn)), where x is the avg moves needed to adjust both heap per each n,
# x will near n if the heap is too big
# 
# binary search
# use an array to replace 2 heaps above, and maintain the array as sorted
# for each n, use binary search to find the index, and insert
# we can leverage data structure that has insert better than O(n) s.t. sortedlist, insert: O(logn)
# overall: O(nlogn), O(n) to visit whole array, for each element O(logn) binary search, O(logn) insert
# 
# merge Sort
# split, if any element crossed (from right to left while merging), i+=1
# O(n*logn)
#
from sortedcontainers import SortedList
from typing import List
import heapq
class Solution:
    # sorted list
    def countSmaller(self, nums:List[int]) -> List[int]:
        sl = SortedList()
        res = []
        for n in nums[::-1]:
            i = sl.bisect_left(n)       # sl[i] >= n
            res.append(i)
            sl.add(n)
        return res[::-1]

    # merge sort
    def countSmaller_MS(self, nums:List[int]) -> List[int]:
        ans = [0 for _ in nums]
        print([(nums[i], i) for i in range(len(nums))])

        def mSort(arr):
            if len(arr) <= 1:
                return arr
            l, r = mSort(arr[:(len(arr)/2)]), mSort(arr[(len(arr)/2):])
            res, i, j = [], 0, 0
            while i < len(l) or j < len(r):
                print(l, r, i, j)
                if j == len(r) or (i < len(l) and l[i][0] <= r[j][0]):
                    ans[l[i][1]] += j
                    res = res + [l[i]]
                    i += 1
                else:
                    res = res + [r[j]]
                    j += 1
            print("output:", res)
            print("ans now:", ans)
            return res

        mSort([(nums[i], i) for i in range(len(nums))])
        return ans

    # heap
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

# print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]) == Solution().countSmaller_DP([1,2,3,4,5,4,3,2,1]))
# print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]))
# print(Solution().countSmaller([1,2,3,4,5,6,7,8,9]))
print(Solution().countSmaller([1,2,3,4,5,6,7,8,9][::-1]))
print(Solution().countSmaller([5,2,6,1]))
print(Solution().countSmaller([1,1,1]))
print(Solution().countSmaller([1]))
print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]))
print(Solution().countSmaller([1,2,3,4,5,6,7,8,9]))