"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # kth smallest: index = k-1
        # kth biggest: index = -k

        # nums.sort()
        sarr = self.mSort(nums)
        # print sarr
        return sarr[-k]

    # implement merge sort
    def mSort(self,arr):
        m = len(arr)//2
        if len(arr) <= 1:
            return arr
        l, r = self.mSort(arr[:m]), self.mSort(arr[m:])
        p1, p2 = 0, 0
        new = []
        while p1<len(l) and p2<len(r):
            if l[p1] <= r[p2]:
                new += l[p1],
                p1 += 1
            else:
                new += r[p2],
                p2 += 1
        while p1<len(l):
            new += l[p1],
            p1 += 1
        while p2<len(r):
            new += r[p2],
            p2 += 1
        return new

print(Solution().findKthLargest([3,2,1,5,6,4] , k = 2))
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6] , k = 4))
print(Solution().findKthLargest([0,1,4,2,3,1,2,3,1,2,31,4,1,3,1,2,3,4,1,2,3,1,2,3] , k = 4))