# for each char, match word, if match => remove that word from word pool and keep going

from typing import List
import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0: return []

        # length need to check
        l = len(words[0])
        L = l*len(words)
        wordCounter = collections.Counter(words)

        def check(s, l):
            if len(s) != L: return False
            split = [s[i:i+l] for i in range(0, len(s), l)]
            c2 = collections.Counter(split)
            return c2 == wordCounter

        ans = []
        for i in range(len(s)):
            if check(s[i:i+L], l):
                ans.append(i)
        
        return ans

print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))