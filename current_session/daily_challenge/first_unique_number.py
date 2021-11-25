from typing import List
import collections
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.dq = collections.deque()
        self.seen = collections.defaultdict(int)
        for n in nums:
            if n not in self.seen: self.dq.append(n)
            self.seen[n] += 1
        
        while self.dq and self.seen[self.dq[0]] > 1:
            self.dq.popleft()
        
        # now dq[0] is unique (or dq is empty)

    def showFirstUnique(self) -> int:
        while self.dq and self.seen[self.dq[0]] > 1:
            self.dq.popleft()
        return self.dq[0] if self.dq else -1

    def add(self, value: int) -> None:
        if value not in self.seen: self.dq.append(value)
        self.seen[value] += 1
        return

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)