'''
503

Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element.

The Next Greater Number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number.

If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

'''
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        stack = []
        ans = [-1 for _ in nums]
        upperBound = max(nums)      # can be optimized within for loop

        # 1st pass
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                x = stack.pop()
                ans[x] = nums[i]
            if nums[i] < upperBound:
                stack.append(i)
        
        # 2nd pass
        for j in range(len(nums)):
            if not stack:
                break
            while stack and nums[j] > nums[stack[-1]]:
                x = stack.pop()
                ans[x] = nums[j]
        return ans

print(Solution().nextGreaterElements([1,2,1]))