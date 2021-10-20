# given constraints: all elements in nums1 and nums2 are unique
# 1 <= nums1.length <= nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 104
# All integers in nums1 and nums2 are unique.
# All the integers of nums1 also appear in nums2.

from typing import List
import heapq
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # create a map/dict of next greater element in nums2
        # key: n, value: index of next greater element than n
        # then simply check the value of all a in nums1
        # how to craft the dict?
        # use a min heap
        # for each element, pop the heap (and assign it as value)
        # until there's no more smaller elements in heap
        # put it into the min heap

        numDict = {}
        minHp = []          # store the value and the index of element
        for i in range(len(nums2)):
            while minHp and minHp[0] < nums2[i]:
                numDict[minHp[0]] = nums2[i]
                heapq.heappop(minHp)
            heapq.heappush(minHp, nums2[i])
        # no next greater element
        for n in minHp:
            numDict[n] = -1
        
        res = []
        for n in nums1:
            if n in numDict:
                res.append(numDict[n])
            else:
                res.append(-1)
        
        return res

print(Solution().nextGreaterElement([4,1,2], nums2 = [1,3,4,2]))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))