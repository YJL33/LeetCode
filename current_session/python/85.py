from typing import List
class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        # leverage monotonic increasing stack

        # convert the original matrix into accumulate matrix (histogram, accumulate along y axis)
        # for each row, accumulate the grid(s) above and change into a histogram
        # find max rectangle for each row
        # 
        # time analysis:
        # O(mn) to traverse whole matrix

        if not mat: return 0
        H, W = len(mat), len(mat[0])
        acc = [[0 for _ in range(W)] for _ in range(H)]
        for j in range(W):
            prev = 0
            for i in range(H):
                if mat[i][j] == "1":
                    prev += 1
                    acc[i][j] = prev
                else:
                    prev = 0
        
        # for each accumulated row, use monotonic increasing stack to find the max rectangle
        # use index instead of height to fill into the stack for easier width calculation
        # while maintaining the stack
        # if incoming h > stack[-1]: append into stack
        # else: POP the stack until the incoming h is the maximum.
        # while poping, calculate the rec
        # h = h[i1] (i1 = popped index), and w = i1-i2 (i2 = stack[-1])
        # 
        # time analysis:
        # overall O(mn) - O(n) to find biggest rectangle in single row, and we have m rows.

        def findMaxRec(hist):
            hist += 0,              # to calculate ractangle with index=W as the right side
            st = []
            zeroIndex = -1          # to calculate rectangle with index=0 as left side
            maxSeen = 0
            for i in range(len(hist)):
                while st and hist[st[-1]] > hist[i]:
                    h = hist[st.pop()]
                    prevI = zeroIndex if not st else st[-1]
                    w = i-(prevI+1)
                    maxSeen = max(maxSeen, h*w)
                st.append(i)
            return maxSeen
        
        # print('acc:', acc)

        return max([findMaxRec(h) for h in acc])

print(Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(Solution().maximalRectangle([]))
# print(Solution().maximalRectangle([["0"]]))
print(Solution().maximalRectangle([["1"]]), 'should be 1')
print(Solution().maximalRectangle([["0","0"]]))