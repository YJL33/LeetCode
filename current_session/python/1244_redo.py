import bisect
import collections
# leverage bisect
class Leaderboard:

    def __init__(self):
        self.scoreDict = collections.defaultdict(list)
        self.arr = []

    def addScore(self, playerId: int, score: int) -> None:
        x = 0
        if playerId in self.scoreDict:
            x = self.scoreDict[playerId]
            self._resetPlayerScoreFromArr(playerId)
        self.scoreDict[playerId] = score+x
        bisect.insort_right(self.arr, score+x)

    def top(self, K: int) -> int:
        return sum(self.arr[-K:])

    def reset(self, playerId: int) -> None:
        if playerId not in self.scoreDict: return
        self._resetPlayerScoreFromArr(playerId)
        return
    
    def _resetPlayerScoreFromArr(self, playerId) -> None:
        toRmv = self.scoreDict[playerId]
        i = bisect.bisect_left(self.arr, toRmv)
        assert(self.arr[i] == toRmv)
        self.arr.pop(i)
        del self.scoreDict[playerId]
        return


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)