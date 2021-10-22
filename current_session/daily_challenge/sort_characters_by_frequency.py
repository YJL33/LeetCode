import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        # create a counter
        charCounter = collections.Counter(s)
        res = []
        for k, v in charCounter.most_common(len(charCounter)):
            res.append(k*v)
        return ''.join(res)
