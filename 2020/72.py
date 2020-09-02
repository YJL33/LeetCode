"""
see https://leetcode.com/problems/edit-distance/
"""
class Solution(object):
    def minDistance(self, w1, w2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # Consider w1(abc) -> w2(defg)
        # At most we can use len(w2) steps to to complete the conversion

        # Use DP
        # say len(w1) = l1, len(w2) = l2
        # create an 2D-array
        # which arr[i][j] represents the required steps for w1[:i+1] -> w2[:j+1]
        # where 0 < i < len(w1), 0 < j < len(w2)
        # initial state: dp[i][j] = j
        # then we evaluate the conversion for l1 substrings -> l2 substrings
        # keep update arr

        #   "" h o r s e      
        # "" 0 1 2 3 4 5  => Deleting these many chars from Horse to make ""
        # r  1 1 2 2 3 4 
        # o  2 2 1 2 3 4 
        # s  3 3 2 2 2 3 
        #    ||
        #    insert these many chars to make a empty string to ros

        dp = [[0 for j in range(len(w2)+1)] for i in range(len(w1)+1)]

        for i in range(len(w1)+1):
            for j in range(len(w2)+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif w1[i-1] == w2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1

        return dp[-1][-1]

print(Solution().minDistance("og", "grs")==3)
print(Solution().minDistance("intention", "execution")==5)
print(Solution().minDistance("sea", "eat") == 2)