import collections
import bisect

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vd = collections.defaultdict(list)
        self.td = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.vd[key].append(value)
        self.td[key].append(timestamp)

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        i = bisect.bisect_right(self.td[key], timestamp)
        if i == 0: return ""
        return self.vd[key][i-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)