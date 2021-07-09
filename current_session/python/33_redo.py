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
        # check whether its in left or right then bs
        head, tail = nums[0], nums[-1]
        if target == head: return 0
        if target == tail: return len(nums)-1
        if target < head < tail or head < tail < target or tail < target < head:
            return -1

        # find pivot
        pvt = self.findPvt(nums)
        # print('pvt',pvt)

        # bs
        if target > head:
            return self.bs(nums[:pvt+1], target)
        else:
            res = self.bs(nums[pvt:], target)
            return res+pvt if res != -1 else res

    def bs(self, arr, tgt):
        l, r = 0, len(arr)-1
        while l < r:
            m = l + (r-l)//2
            # print('l,r,m,arr,arr[m],tgt',l,r,m,arr,arr[m],tgt)
            if arr[m]==tgt:
                return m
            elif arr[m]>tgt:    # arr[m] is bigger than tgt
                r = m           # in the smaller half
            else:
                l = m+1         # in the bigger half
        return -1 if arr[l]!= tgt else l

    def findPvt(self, arr):
        l, r = 0, len(arr)-1
        if arr[l] < arr[r]: return len(arr)-1
        while l < r:
            m = l + (r-l)//2
            # compare arr[l:m] and arr[m+1:r]
            # print('m',m)
            if arr[l]<=arr[m] and arr[m+1]<=arr[r]:
                return m
            elif arr[m]<=arr[l]:
                r = m
            else:
                l = m+1
        return len(arr)-1


print(Solution().search([1,2,3,4,5,6],4), 'should be 3')
print(Solution().search([4,5,6,7,0,1,2], 0), 'should be 4')
print(Solution().search([4,5,6,7,0,1,2], 5), 'should be 1')
print(Solution().search([1,2,3,4,5,6,7], 3), 'should be 2')
print(Solution().search([2], 1), 'should be -1')
print(Solution().search([1], 1), 'should be 0')
print(Solution().search([0], 1), 'should be -1')
print(Solution().search([3,1], 1), 'should be 1')
print(Solution().search([3,1], 3), 'should be 0')
print(Solution().search([1,3], 0), 'should be -1')
print(Solution().search([3,1], 0), 'should be -1')
print(Solution().search([3,5,1],5), 'should be 1')
print(Solution().search([3,5,1],0), 'should be -1')