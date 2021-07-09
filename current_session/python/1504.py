"""
see https://leetcode.com/problems/count-submatrices-with-all-ones/
"""
class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        #precipitate mat to histogram 
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0: 
                    mat[i][j] += mat[i-1][j]    # histogram 
        
        ans = 0
        for x in mat: print(x)
        for i in range(m):
            stack = []                          # mono-stack of indices of non-decreasing height
            cnt = 0
            for j in range(n):
                # print("i, j:", i,j)
                # print('befor: ', cnt)
                
                # handle column by column
                while stack and mat[i][stack[-1]] > mat[i][j]: 
                    jj = stack.pop()                            # start
                    kk = stack[-1] if stack else -1             # end
                    # print("here we are! jj, kk", jj, kk)
                    cnt -= (mat[i][jj] - mat[i][j])*(jj - kk)   # adjust to reflect lower height

                cnt += mat[i][j]                                # count submatrices bottom-right at (i, j)
                ans += cnt
                stack.append(j)                                 # add each column here
                # print('after: ', cnt)
                # print('ans, stack', ans, stack)

        return ans

# print(Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]]), 'sb 13')
# print(Solution().numSubmat([[1,1,0],[1,1,1],[1,1,1]]), 'sb 27')
print(Solution().numSubmat([[1,1,0],[0,1,1],[1,1,1]]), 'sb 17')
print(Solution().numSubmat([[1,1,1],[0,1,0],[1,0,1]]), 'sb 10')
print(Solution().numSubmat([[1,1,1],[0,1,1],[1,0,1]]), 'sb 16')
# print(Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]), 'sb 24')
# print(Solution().numSubmat([[1,1,0,1,1,1,1,0,1],[0,1,1,1,1,0,1,1,0],[1,0,0,0,0,1,1,1,1],[0,0,1,0,1,1,1,1,1],[0,0,0,1,0,1,1,1,1],[0,0,1,0,0,1,0,1,0]]), 'sb 122')