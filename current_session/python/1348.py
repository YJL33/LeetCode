"""
1348
"""
# use a dictionary and binary search
import collections
import bisect
class TweetCounts(object):
    def __init__(self):
        self.td = collections.defaultdict(list)
        self.fd = {'minute': 60,'hour': 60*60,'day': 60*60*24,}

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        bisect.insort_left(self.td[tweetName], time)

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        # beware the frequency
        start = bisect.bisect_left(self.td[tweetName], startTime)
        end = bisect.bisect_right(self.td[tweetName], endTime)
        span = self.fd[freq]
        ans = [0 for _ in range(((endTime-startTime)//span)+1)]
        i = 0
        for t in self.td[tweetName][start:end]:
            while t-startTime >= (i+1)*span: i += 1
            ans[i] += 1
        return ans

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)