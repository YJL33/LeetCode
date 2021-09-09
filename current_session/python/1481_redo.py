# use counter
import collections
from typing import List
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k >= len(arr): return 0
        numCounter = collections.Counter(arr)
        
        # use buckets here, bucket index = count
        buckets = [[] for _ in range(len(arr)+1)]
        for char, count in numCounter.items():
            buckets[count].append(char)
        
        for cnt in range(len(arr)+1):
            if k == 0: break
            while len(buckets[cnt]) > 0 and k >= cnt:
                char = buckets[cnt].pop()
                del numCounter[char]
                k -= cnt

        return len(numCounter)

print(Solution().findLeastNumOfUniqueInts([5,5,4],1))