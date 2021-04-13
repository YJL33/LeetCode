"""
1244
"""
import collections
import bisect
from typing import List
class Leaderboard:

    def __init__(self):
        self.lb = collections.defaultdict(int)
        self.arr = []

    def addScore(self, playerId: int, score: int) -> None:
        x = 0
        if playerId in self.lb:
            x += self.lb[playerId]
            self._removeScore(playerId)

        self.lb[playerId] = score+x
        bisect.insort_right(self.arr, score+x)
        return

    def top(self, K: int) -> int:
        # print(self.arr, self.arr[-K:])
        return sum(self.arr[-K:])

    def reset(self, playerId: int) -> None:
        if playerId not in self.lb:
            return
        self._removeScore(playerId)
    
    def _removeScore(self,playerId) -> None:
        # print('lb', self.lb)
        # print('arr:', self.arr)
        # print('player:', playerId)
        prevScore = self.lb[playerId]
        j = bisect.bisect_left(self.arr, prevScore)
        assert(self.arr[j] == prevScore)
        self.arr.pop(j)
        del self.lb[playerId]
        return

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)