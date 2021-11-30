import collections
import bisect
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ss, st = set(source), set(target)
        if not st.issubset(ss): return -1
        sd = collections.defaultdict(list)
        for i in range(len(source)):
            sd[source[i]].append(i)
        
        prevI = -1
        cnt = 1
        for i in range(len(target)):
            listOfIndexes = sd[target[i]]
            j = bisect.bisect_right(listOfIndexes, prevI)
            if j == len(listOfIndexes):
                cnt += 1
                nextIndex = listOfIndexes[0]
            else:
                nextIndex = listOfIndexes[j]
            prevI = nextIndex
        return cnt

print(Solution().shortestWay('abc', 'abcbc'))
print(Solution().shortestWay('abc', 'acdbc'))
print(Solution().shortestWay('xyz', 'xzyxz'))