class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 'connect' each person in M (naive approach) then count groups

        ans = [i for i in range(len(M))]
        for i in range(len(M)):
            for j in range(i+1, len(M[0])):
                if M[i][j] == 1:
                    # assign j'root to i's root
                    r1, r2 = i, j
                    while r1 != ans[r1]:
                        r1 = ans[r1]
                    while r2 != ans[r2]:
                        r2 = ans[r2]
                    ans[r2] = r1

        return sum([1 if i == ans[i] else 0 for i in range(len(ans))])

print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,1,0],[1,1,1],[0,1,1]]))
print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))