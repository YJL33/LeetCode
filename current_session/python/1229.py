# simply scan through whole slots1 and slots2
# (or we can simply use 2 cursors)
# 
# if both slots are available, check if duration is meet.
# if not, then move cursor go to next one

from typing import List

# in case we want to save O(m) space from merging slots1 and slots2
# implement our own iterator, __iter__ and __next__, and maintain 2 cursors inside
class Events:
    def __init__(self, e1, e2):
        self.max = len(e1)+len(e2)
        self.e1 = e1
        self.e2 = e2
    def __iter__(self):
        self.c1 = 0
        self.c2 = 0
        return self
    def __next__(self):
        if self.c1//2+self.c2//2 < self.max:
            t1 = self.e1[self.c1//2][self.c1%2] if self.c1//2 < len(self.e1) else -1
            t2 = self.e2[self.c2//2][self.c2%2] if self.c2//2 < len(self.e2) else -1
            # print('t1, t2', t1, t2, self.c1, self.c2)
            if t1 == -1:
                self.c2 += 1
                return t2, 's' if self.c2%2 else 'e'
            elif t2 == -1:
                self.c1 += 1
                return t1, 's' if self.c1%2 else 'e'
            elif t2 < t1:
                self.c2 += 1
                return t2, 's' if self.c2%2 else 'e'
            else:
                self.c1 += 1
                return t1, 's' if self.c1%2 else 'e'  
        raise StopIteration
            
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        # for the sake of simplicy, merge both slots
        events = []
        for s, e in slots1:
            events.append((s, 's'))
            events.append((e, 'e'))
        for s, e in slots2:
            events.append((s, 's'))
            events.append((e, 'e'))
        events.sort()
        
        # Optimization: maintain 2 cursors to save O(m) space
        # slots1.sort()
        # slots2.sort()
        # events = Events(slots1, slots2)
        
        avail = 0
        can_start = None
        for event_time, event_type in events:
            if event_type == 's':
                avail += 1
                if avail == 2:
                    can_start = event_time
            else:
                if avail == 2:
                    if event_time - can_start >= duration:
                        return [can_start, can_start+duration]
                avail -= 1
        return []

print(Solution().minAvailableDuration([[216397070,363167701],[98730764,158208909],[441003187,466254040],[558239978,678368334],[683942980,717766451]],[[50490609,222653186],[512711631,670791418],[730229023,802410205],[812553104,891266775],[230032010,399152578]],456085))
print(Solution().minAvailableDuration([[0,20]],[[1,2],[4,30]],4))
print(Solution().minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))