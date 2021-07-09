"""
see https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """           
        res = sum(cardPoints[:k])
        if k == len(cardPoints):
            return res
        # pick i from right and pick k-i from left
        ls, rs = res, 0
        for i in range(1,k+1):
            rs += cardPoints[-i]
            ls -= cardPoints[k-i]
            res = max(res, ls+rs)
            # print(res, ls, rs)
        return res

print(Solution().maxScore([9,7,7,9,7,7,9],6))