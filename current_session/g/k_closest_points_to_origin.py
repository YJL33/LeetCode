from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k:int) -> List[List[int]]:
        # calculate the distance to origin for each points
        # sort by distance
        # then pick K closest 
        distAndPnt = []
        for i in range(len(points)):
            a, b = points[i]
            distAndPnt.append((a*a+b*b, i))
        distAndPnt.sort()
        # print(distAndPnt)

        return [points[i] for _,i in distAndPnt[:k]]

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))
print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
