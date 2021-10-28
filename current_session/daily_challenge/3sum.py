from typing import List
import collections
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # leverage negative numbers
        if not nums: return []
        nums.sort()
        i = 0
        res = []

        # find the corresponding 2-sum
        def finder(target, start):
            numDict = collections.defaultdict()
            seen = set()
            for i in range(start, len(nums)):
                y = target-nums[i]
                if y in numDict and y <= nums[i] and (y, nums[i]) not in seen:
                    j = numDict[y]
                    seen.add((nums[j], nums[i]))
                numDict[nums[i]] = i
            return [[-1*target, a, b] for a, b in seen]

        while i < len(nums) and nums[i] <= 0:
            target = -1*nums[i]
            tmp = finder(target, i+1)
            if len(tmp):
                for x in tmp:
                    res.append(x)
            while i < len(nums) and nums[i] == -1*target:
                i += 1
        
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))
print(Solution().threeSum([-1,0,-2,-3,-4,1,2,3,4,5,1,2,3,4,1,2,3]))