"""
33
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot and then find target
        def findPvt(arr):
            l, r = 0, len(arr)-1
            if arr[l] < arr[r]: return len(arr)-1
            while l < r:
                m = l + (r-l)//2
                # find target
                if nums[m] > nums[m+1]: return m
                if nums[m] > nums[0]:       # pvt at right
                    l = m+1
                else:                       # pvt at left
                    r = m
            return l
        
        def bs(arr, tgt):
            l, r = 0, len(arr)-1
            while l < r:
                m = l + (r-l)//2
                if arr[m]==tgt:
                    return m
                if arr[m] < tgt:
                    l = m+1
                else:
                    r = m
            return l if 0 <= l < len(arr) and arr[l] == tgt else -1
     
        pvt = findPvt(nums)

        if target >= nums[0]:
            ans = bs(nums[:pvt+1], target)
        else:
            ans = bs(nums[pvt+1:], target) + pvt+1
        
        return ans if ans < len(nums) and nums[ans] == target else -1

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
print(Solution().search([1,3], 1), 'should be 0')
print(Solution().search([1,3], 3), 'should be 1')
print(Solution().search([3,1], 0), 'should be -1')
print(Solution().search([3,5,1],5), 'should be 1')
print(Solution().search([3,5,1],0), 'should be -1')