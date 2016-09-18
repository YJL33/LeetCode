"""
 401. Binary Watch

    User Accepted: 13
    User Tried: 27
    Total Accepted: 13
    Total Submissions: 45
    Difficulty: Easy

A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on,
return all possible times the watch could represent.
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # hour: 0-3
        # [1,2,4,8], [3,5,6,9,10,12], [7,11]
        # min: 0-5
        # [1,2,4,8,16,32]

        if num > 8:
            return []
        if num == 1:
            return ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

        hrbase, minbase = [1,2,4,8], [1,2,4,8,16,32]
        res = []
        for i in xrange(4):
            numofhr, numofmin = i, num-i
            hrs, mins = [], []
            self.getNum(numofhr, 11, hrbase, hrs)
            self.getNum(numofmin, 59, minbase, mins)
            #print numofhr, numofmin, hrs, mins
            for h in hrs:
                for m in mins:
                    time = "{}:".format(h)+str(m).zfill(2)
                    res.append(time)

        return res

    def getNum(self, n, limit, base, res, pathsum=0):
        # get the possible number of n from base
        if len(base) < n or pathsum > limit:
            return
        if n == 0 and pathsum == 0:
            res.append(0)
            return
        elif len(base) == n and pathsum+sum(base) <= limit:
            res.append(pathsum+sum(base))
            return
        if n == 0:
            res.append(pathsum)
            return
        for i in xrange(len(base)):
            self.getNum(n-1, limit, base[i+1:], res, pathsum+base[i])
