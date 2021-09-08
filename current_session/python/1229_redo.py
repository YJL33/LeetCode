# simply scan through whole slots1 and slots2
# (or we can simply use 2 cursors)
# 
# if both slots are available, check if duration is meet.
# if not, then move cursor go to next one

from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        # slots1 and slot2 are not sorted....
        events = []
        for s, e in slots1:
            events.append((s, 's'))
            events.append((e, 'e'))
        for s, e in slots2:
            events.append((s, 's'))
            events.append((e, 'e'))
        events.sort()

        availCnt, canStart = 0, None
        for i in range(len(events)):
            t, type = events[i]
            availCnt += 1 if type == 's' else -1
            if availCnt == 2:
                canStart = t
            elif availCnt == 1 and canStart is not None:
                if t-canStart >= duration:
                    return [canStart,canStart+duration]
                else:
                    canStart = None

        return []

print(Solution().minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],[[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],456085))
print(Solution().minAvailableDuration([[0,20]],[[1,2],[4,30]],4))
print(Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))