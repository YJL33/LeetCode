"""
1010
"""
import collections
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # get number of pair of songs that's divisible by 60
        # get mod and use dict

        songDict = collections.defaultdict(int)    # key: mod 60, value: count
        for i in range(len(time)):
            tm = time[i]%60
            songDict[tm] += 1
        
        ts = songDict.keys()
        ans = 0
        for t in ts:
            if t == 0 or t == 30:
                N = songDict[t]
                ans += N*(N-1)/2
            
            elif t < 30 and (60-t) in songDict:
                N, M = songDict[t], songDict[60-t]
                ans += N*M

        return ans
