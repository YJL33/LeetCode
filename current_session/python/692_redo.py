import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        return [a[0] for a in cnt.most_common(k)]