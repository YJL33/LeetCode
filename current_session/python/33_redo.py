from typing import List
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check special case
        if len(nums) == 1: return 0 if nums[0] == target else -1

        def find_pivot(arr):
            if arr[0] < arr[-1]:        # no sort
                return 0
            l, r = 0, len(arr)          # use 2nd template
            while l < r:
                m = (l+r+1)//2          # variance of r side
                if arr[m] < arr[m-1]:
                    return m
                elif arr[m] > arr[0]:   # m is too big
                    l = m
                else:
                    r = m-1            
            return -1

        min_index, x = find_pivot(nums), 0
        if target >= nums[0]:
            tmp = nums[:min_index] if min_index != 0 else nums
            x = bisect.bisect_left(tmp, target)
        else:
            x = min_index + bisect.bisect_left(nums[min_index:], target)
        return x if x < len(nums) and nums[x] == target else -1


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