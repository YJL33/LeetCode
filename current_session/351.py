"""
351
"""
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        rd = {(1,3):2, (4,6):5, (7,9):8, (1,9):5, (3,7):5, (1,7):4, (2,8):5, (3,9):6}
        res = [[], [[a] for a in range(1,10)]]
        allN = set([a for a in range(1,10)])
        for _ in range(2,n+1):
            newPattern = []
            for base in res[-1]:
                used = set(base)
                avail = allN.difference(used)
                last = base[-1]
                for a in avail:
                    x, y = min(last, a), max(last, a)
                    if (x, y) in rd and rd[(x,y)] not in used: continue
                    newPattern.append(base+[a])
            res += newPattern,
        
        return sum([len(x) for x in res[m:n+1]])

print(Solution().numberOfPatterns(1,2))
print(Solution().numberOfPatterns(2,2))