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
        td = collections.defaultdict(int)
        for i in range(len(time)):
            td[time[i]%60] += 1
        
        cnt = 0
        for k, v in td.items():
            if k == 0 or k == 30:
                cnt += v*(v-1)//2
            if k < 30 and 60-k in td:          # combination = 2
                cnt += v*(td[60-k])
        return cnt

