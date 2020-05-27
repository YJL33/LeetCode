"""
494. Target Sum

    User Accepted: 247
    User Tried: 348
    Total Accepted: 254
    Total Submissions: 812
    Difficulty: Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

    The length of the given array is positive and will not exceed 20.
    The sum of elements in the given array will not exceed 1000.
    Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # TLE
        def dfs(i, tgt):
            if i == len(nums): return 1 if (tgt == 0) else 0
            return dfs(i+1, tgt-nums[i])+dfs(i+1, tgt+nums[i])
        return dfs(0, S)

    
    def findTargetSumWays2(self, nums, S):
        numofways, way, cnt, tmp = 1<<(len(nums)), 0, 0, -sum(nums)
        # 0: negative, 1: positive
        while way+1 < numofways:
            change, i = way^(way+1), 0
            while change:
                # print change, i
                if change&1:
                    tmp = tmp-2*nums[i] if way&(1<<i) else tmp+2*nums[i]
                change, i = change>>1, i+1
            if tmp == S: cnt += 1
            way += 1
        return cnt
