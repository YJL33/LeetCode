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
        if num > 8: return []

        res, hrbase, minbase = [], [1,2,4,8], [1,2,4,8,16,32]
        for i in xrange(4):
            numofhr, numofmin, hrs, mins = i, num-i, [], [] 
            self.getNum(numofhr, 11, hrbase, hrs)
            self.getNum(numofmin, 59, minbase, mins)
            for h in hrs:
                for m in mins:
                    time = "{}:".format(h)+str(m).zfill(2)
                    res.append(time)
        return res

    def getNum(self, n, limit, base, reads, pathsum=0):
        if len(base) < n or pathsum > limit:
            return
        if n == 0 and pathsum == 0:
            reads.append(0)
            return
        elif len(base) == n and pathsum+sum(base) <= limit:
            reads.append(pathsum+sum(base))
            return
        if n == 0:
            reads.append(pathsum)
            return
        for i in xrange(len(base)):
            self.getNum(n-1, limit, base[i+1:], reads, pathsum+base[i])
