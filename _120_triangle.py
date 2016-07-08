"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        num_of_layer = len(triangle)
        
        # 1st pass: from bottom layer to top layer, pick the best route for the next layer
        # e.g.
        # [
        #       [2],            layer 0
        #      [3,4],                 1
        #     [6,5,7],                2
        #    [4,1,8,3]                3
        # ]
        #
        # in layer 3, pick [1,1,3] for layer 2
        #
        # 2nd pass: add-up and repeat 1st pass

        pick = []

        for layer in reversed(triangle):
            res = layer
            if pick:
                for j in xrange(len(layer)):        # 2nd pass
                    res[j] += pick[j]
                pick = []
            for i in xrange(len(layer)-1):          # 1st pass
                pick += min(res[i], res[i+1]),

        return res[0]




