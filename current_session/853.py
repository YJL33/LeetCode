"""
853
"""
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # check all car for pos and speed
        # if a behind b and a faster than b, see if they'll meet before destination
        # if so, -1 fleet

        numOfFleet = len(position)
        # tailor pos and speed together
        cars = [(position[i],speed[i]) for i in range(len(speed))]
        cars.sort()
        print(cars)
        
        prev, x = numOfFleet-1, numOfFleet-2
        while x >= 0:
            # see if cars[x] and cars[prev] in the same fleet
            print('prev, x', prev, x)
            if cars[x][1] > cars[prev][1]:
                t = 1.0*(cars[prev][0]-cars[x][0])/(cars[x][1]-cars[prev][1])
                if t >= 0 and (cars[x][0] + cars[x][1]*t) <= target:
                    numOfFleet -= 1
                    x -= 1
                    continue                
            prev, x = x, x-1
        
        return numOfFleet

print(Solution().carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))