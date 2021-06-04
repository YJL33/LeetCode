"""
1348
"""
import collections
from typing import List
class TweetCounts:

    def __init__(self):
        self.td = collections.defaultdict(list)
        self.fd = {'minute':60, 'hour':3600, 'day':86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.td[tweetName].append(time)
        return

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        freqInSec = self.fd[freq]
        L = (endTime-startTime)//freqInSec + 1
        res = [0 for _ in range(L)]
        for t in self.td[tweetName]:
            if startTime<=t<=endTime:
                res[(t-startTime)//freqInSec] += 1
        return res
        

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)