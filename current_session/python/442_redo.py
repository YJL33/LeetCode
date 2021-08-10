from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # leverage array itself as hashmap:
        # note that there are n integers and all integers are in the range [1,n]
        # key: use num[i]-1 as index, value: bool, negative as visited

        res = []
        for i in range(len(nums)):
            n = abs(nums[i])            # use abs in case it's converted
            ind = n-1
            if nums[ind] < 0:
                res.append(n)
            else:
                nums[ind] = -1*nums[ind]
        return res
