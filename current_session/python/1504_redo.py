from typing import List

# convert to histogram first
# use monotonic stack

# e.g.
#  [1,0,1]    [1,0,1]    1+1 
#  [1,1,0] => [2,1,0] => 2+1+(1)    (consecutive 2)
#  [1,1,1]    [3,2,1] => 3+2+(2*1)+1+(1+1)  (consecutive 2), (consecutive 3)
# for each row, calculate the rectangles

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # convert to histogram first
        H, W = len(mat), len(mat[0])
        for i in range(1,H):
            for j in range(W):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i-1][j]
        
        # print("mat:", mat)
        
        count = 0
        for i in range(H):
            mStack = []         # monotonic stack with non-decreasing height
            tmp = 0
            for j in range(W):
                while mStack and mat[i][mStack[-1]] > mat[i][j]:
                    jj = mStack.pop()
                    kk = mStack[-1] if mStack else -1
                    tmp -= (mat[i][jj] - mat[i][j])*(jj - kk)
                tmp += mat[i][j]
                count += tmp
                mStack.append(j)
                # print("i:", i, "j:", j, "stack:", mStack, "cnt:", count)

        return count

print(Solution().numSubmat([[1,0,1],[1,1,0],[1,1,0]]), 'sb 13')
print(Solution().numSubmat([[1,1,0],[0,1,1],[1,1,1]]), 'sb 17')
print(Solution().numSubmat([[1,1,1],[0,1,0],[1,0,1]]), 'sb 10')
print(Solution().numSubmat([[1,1,1],[0,1,1],[1,0,1]]), 'sb 16')
