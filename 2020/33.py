"""
see https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot first
        p = self.findPivot(nums)

        # print('p', p)
        # print('nums, t', nums, target)
        res = 0
        if nums[0]<=target:
            # print('case 1')
            res = self.bs(nums, target, 0, p)
        else:
            # print('case 2')
            res = self.bs(nums, target, p+1, len(nums)-1)

        if res < 0: res += len(nums)

        return res if nums[res] == target else -1

    def findPivot(self, arr):
        p = 0
        while p+1<len(arr) and arr[p]<arr[p+1]:
            p += 1
        return p

    def bs(self, arr, t, l, r):
        if not arr: return 0
        while l < r:
            m = (r+l)//2
            if arr[m] == t:
                return m
            elif arr[m] > t:
                r = m
            else:
                l = m+1

        # in case l is good
        if l < len(arr) and arr[l] == t:
            return l

        print("we're here...")
        print('bs:', l-1)
        res = max(0,l-1)
        return res if arr[res] == t else -1


print(Solution().search([4,5,6,7,0,1,2], 0), 'should be 4')
print(Solution().search([4,5,6,7,0,1,2], 5), 'should be 1')
print(Solution().search([1,2,3,4,5,6,7], 3), 'should be 2')
print(Solution().search([2], 1), 'should be -1')
print(Solution().search([1], 1), 'should be 0')
print(Solution().search([0], 1), 'should be -1')
print(Solution().search([3,1], 1), 'should be 1')
print(Solution().search([3,1], 3), 'should be 0')
print(Solution().search([3,5,1],5), 'should be 1')
