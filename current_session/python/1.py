"""
see https://leetcode.com/problems/two-sum/
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force:
        # simply try all i, j for 0<=i,j<len(nums); see if there's nums[i]+nums[j] == target
        # time analysis: O(n^2)

        # better approach:
        # visit whole array and use hashmap (python dictionary) to store seen elements
        # key: number itself, value: index
        # time analysis: O(n) to visit the array, O(1) to store/check the dictionary (worst case O(n) if there's a hash collision)
        # space analysis: O(n) (worst case O(n))
        
        seen = {}
        for i,n in enumerate(nums):
            if target-n in seen:                    # we've seen the counter-part of n, get the index by value
                return [i, seen[target-n]]
            else:
                seen[n] = i                         # it'll be fine to replace it
        return []                                   # shouldn't reach this line

print(Solution().twoSum([4, 6, 7, 11, 5], 12))
