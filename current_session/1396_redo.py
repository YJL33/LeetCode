"""
1396
"""
import collections
class UndergroundSystem:

    def __init__(self):
        self.pd = collections.defaultdict(tuple)    # key: person ID, val: (startStation, checkInTime)
        self.rd = collections.defaultdict(list)     # key: start-end pair, val:list of trips

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.pd[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        startStation, checkInTime = self.pd[id]
        self.rd[(startStation, endStation)].append(t-checkInTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.rd[(startStation, endStation)])/len(self.rd[(startStation, endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)