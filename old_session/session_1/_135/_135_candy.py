"""
135. Candy

    Total Accepted: 59690
    Total Submissions: 253395
    Difficulty: Hard
    Contributors: Admin

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # O(n)
        if not ratings: return 0
        # 1st pass
        L, res = len(ratings), [1 for _ in ratings]
        for i in xrange(1,L):
            if ratings[i] > ratings[i-1]:           # res[i] should > res[i-1]
                res[i] = res[i-1]+1                 # increase it by 1
        # 2nd pass
        for j in xrange(L-1,0,-1):
            if ratings[j-1] > ratings[j]:           # res[i-1] should > res[i]
                res[j-1] = max(res[j-1], res[j]+1)  # increase it by minimum

        return sum(res)