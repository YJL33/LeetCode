"""
417
"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []

        H, W = len(matrix), len(matrix[0])
        pacSet, atlSet = set(), set()

        # add the spot and check its neighbors
        def checker(r, c, fromPac=True):
            if fromPac:
                pacSet.add((r,c))
            else: 
                atlSet.add((r,c))

            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            for n in neighbors:
                p, q = r+n[0], c+n[1]
                if fromPac and (p,q) in pacSet:
                    continue
                if not fromPac and (p,q) in atlSet:
                    continue
                if 0<=p<H and 0<=q<W and matrix[p][q] >= matrix[r][c]:
                    checker(p,q,fromPac)
                    

        # check pacific
        for i in range(H):
            for j in range(W):
                if i==0 or j==0:
                    checker(i,j)
        
        # check atlantic
        for i in range(H-1, -1, -1):
            for j in range(W-1, -1, -1):
                if i==H-1 or j==W-1:
                    checker(i,j,False)

        # return the intersection of both set
        # print('pac:', pacSet)
        # print('atl:', atlSet)
        return pacSet.intersection(atlSet)

print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))