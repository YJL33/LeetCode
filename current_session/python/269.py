from typing import List
import collections
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # graph:
        # a -> b means a is lexicographically before b
        # construct the graph first
        # dict: key=char, val= set of those after char

        cd1 = collections.defaultdict(set)      # key before val
        cd2 = collections.defaultdict(set)      # key after val
        seen = set(''.join(words))
        # seenAfter = set()
        for j in range(len(words)):
            for k in range(j+1, len(words)):
                w1, w2, index = words[j], words[k], 0
                while index < min(len(w1), len(w2)) and w1[index] == w2[index]: index += 1
                if index < min(len(w1), len(w2)):
                    c1, c2 = w1[index], w2[index]
                    cd1[c1].add(c2)
                    cd2[c2].add(c1)
                    # seenAfter.add(c2)
                else:
                    if len(w2) < len(w1): return ""
        
        # begin from seen-seenafter
        # seenAfter is as same as set(cd2.keys())
        initials = seen.difference(set(cd2.keys()))
        # print('ini:', initials)
        if not initials: return ""

        ans = ''
        while initials:
            a = initials.pop()
            ans += a
            for b in cd1[a]:
                cd2[b].remove(a)
                if not cd2[b]:
                    initials.add(b)
        
        return ans if len(ans) == len(seen) else ""

print(Solution().alienOrder(["wrt","wrf","er","ett","rftt"]), '== wertf')
print(Solution().alienOrder(['z', 'x']), '== zx')
print(Solution().alienOrder(["z","x","z"]) , '== ')
print(Solution().alienOrder(["z","z"]), '== z')
print(Solution().alienOrder(["zy","zx"]), '== yxz')
print(Solution().alienOrder(["abc","ab"]), '== ""')
