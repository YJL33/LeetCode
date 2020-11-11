"""
see https://leetcode.com/problems/design-underground-system/
"""
class UndergroundSystem(object):

    def __init__(self):
        self.AToB = collections.defaultdict(list)
        self.userDict = collections.defaultdict(list)

    # when check-in: put it into a dictionary (user)
    # key: user-id val: (station, time)
    def checkIn(self, userId, stationName, t):
        """
        :type userId: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.userDict[userId] = [stationName, t]
        
    # when check-out: put it into a dictionary (travel time)
    # key: start-end val: [time spent]
    def checkOut(self, userId, checkOutAt, t):
        """
        :type userId: int
        :type checkOutAt: str
        :type t: int
        :rtype: None
        """
        if userId in self.userDict:
            checkInAt, startTime = self.userDict[userId]
            self.AToB[(checkInAt, checkOutAt)].append(t-startTime)
        
    # query the time spant dictionary
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        if (startStation, endStation) in self.AToB:
            trips = self.AToB[(startStation, endStation)]
            return (1.0*sum(trips))/len(trips)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)