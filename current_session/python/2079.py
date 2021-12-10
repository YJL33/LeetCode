from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # simply simulate the process
        step = 0
        remaining = capacity
        for i in range(len(plants)):
            needed = plants[i]
            if remaining >= needed:
                step += 1
                remaining -= needed
            else:
                step += 2*i+1
                remaining = capacity - needed
            # print('i:', i, 'steps:', step)
        return step


print(Solution().wateringPlants([2,2,3,3], capacity = 5), 'should be 14')
print(Solution().wateringPlants([1,1,1,4,2,3], capacity = 4), 'should be 30')
print(Solution().wateringPlants([7,7,7,7,7,7,7], 8), 'should be 49')
print(Solution().wateringPlants([3,2,4,2,1],6), 'should be 17')