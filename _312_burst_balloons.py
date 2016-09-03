"""
312. Burst Balloons

Given n balloons, indexed from 0 to n-1.
Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i.
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≦ n ≦ 500, 0 ≦ nums[i] ≦ 100

Example:

Given [3, 1, 5, 8]
Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
class Solution(object):
    def maxCoins(self, numlist):
        """
        :type numlist: List[int]
        :rtype: int
        """
        nums = [1] + [i for i in numlist if i > 0] + [1]        # burst zero balloons
        n = len(nums)                                           # number of non-zero balloons
        dp = [[0]*n for _ in xrange(n)]     # dp[i][j] = max coins can get from between pos i & j

        for k in xrange(2, n):                                  # span (from left to right)
            for left in xrange(0, n-k):
                right = left + k
                for i in xrange(left+1,right):
                    dp[left][right] = max(dp[left][right],
                        nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
        return dp[0][n-1]

        # https://goo.gl/qOdFaM
        # Note that we put 2 balloons with 1 as boundaries,
        # and also burst all the zero balloons in the first round since they won't give any coins.
        # The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.
        # for the example [3, 1, 5, 8], the dp matrix is updated like this
        # 
        # 0    0    0    0    0    0
        # 0    3    0    0    0    0
        # 0    0    15   0    0    0
        # 0    0    0    40   0    0
        # 0    0    0    0    40   0
        # 0    0    0    0    0    0
        # 
        # then
        # 
        # 0    0    0    0    0    0
        # 0    3    30   0    0    0
        # 0    0    15   135  0    0
        # 0    0    0    40   48   0
        # 0    0    0    0    40   0
        # 0    0    0    0    0    0
        # 
        # at last
        # 
        # 0    0    0    0    0    0
        # 0    3    30   159  167  0
        # 0    0    15   135  159  0
        # 0    0    0    40   48   0
        # 0    0    0    0    40   0
        # 0    0    0    0    0    0
