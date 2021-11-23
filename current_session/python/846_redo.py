from typing import List
import collections
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # is there a O(N) solution?
        if len(hand)%groupSize != 0: return False
        # O(NlogN) solution
        # sort then check by groupSize

        handCount = collections.Counter(hand)
        numOfStraights = len(hand)//groupSize
        # print('ns:', numOfStraights)

        uniqueH, i = [k for k in handCount.keys()], 0
        uniqueH.sort()

        # pick straights from hands
        while numOfStraights > 0:
            
            while handCount[uniqueH[i]] == 0: i += 1
            nextH, toAdd = uniqueH[i], groupSize

            while toAdd > 0:
                # print('nextH', nextH)
                if nextH not in handCount or handCount[nextH] == 0:
                    return False
                else:
                    handCount[nextH] -= 1
                    nextH, toAdd = nextH+1, toAdd-1
            
            numOfStraights -= 1
        
        return True

# print(Solution().isNStraightHand())
print(Solution().isNStraightHand([8,10,12],3))
print(Solution().isNStraightHand([1,2,3,4,5],4))
print(Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3))

