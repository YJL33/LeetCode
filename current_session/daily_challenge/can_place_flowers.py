from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # simply go through the whole array
        cnt = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(len(flowerbed)):
            f = flowerbed[i]
            if f == 1:
                cnt = 0
                continue
            cnt += 1
            # only plant when we see 3, 5, 7.....
            if (cnt-3)>=0 and (cnt-3)%2 == 0:
                n -= 1
            if n == 0:
                return True

        return False