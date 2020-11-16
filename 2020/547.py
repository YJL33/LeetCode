"""
https://leetcode.com/problems/friend-circles/
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # use an array to link all direct friends
        arr = [i for i in range(len(M))]

        # i < j always holds
        for i in range(len(M)):
            for j in range(i+1,len(M[0])):
                if M[i][j]:
                    # here we want to make sure that i and j has same root
                    # assign the root of (j's root) with i's root
                    iRoot, ii = arr[i], i
                    while iRoot != ii:
                        ii = arr[ii]
                        iRoot = arr[ii]
                    jRoot, jj = arr[j], j
                    while jRoot != jj:
                        jj = arr[jj]
                        jRoot = arr[jj]
                    arr[jj] = iRoot

        ans = 0
        # check arr
        for i in range(len(arr)):
            if arr[i] == i:
                ans += 1

        return ans

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))