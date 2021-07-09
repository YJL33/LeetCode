"""
767
"""
import collections
class Solution:
    def reorganizeString(self, s: str) -> str:
        # count
        cnt = collections.Counter(s)
        _, mccnt = cnt.most_common(1)[0]
        if (len(s) % 2 and mccnt > len(s)/2 + 1) or (len(s) % 2 == 0 and mccnt > len(s)/2):
            return ""
        
        # fill the string, first put the most common one, then the rest
        st = cnt.most_common()
        st.reverse()
        order = [a for a in range(0,len(s),2)] + [b for b in range(1,len(s),2)]
        res = ['' for _ in order]
        i = 0
        while st:
            char, cnt = st.pop()
            while cnt:
                # print('res, order[i], char, cnt', res, order[i], char, cnt)
                res[order[i]], cnt, i = char, cnt-1, i+1
        return ''.join(res)

print(Solution().reorganizeString('aab'))
print(Solution().reorganizeString('aaab'))
print(Solution().reorganizeString('aabb'))
print(Solution().reorganizeString("aaaaaaaabbccdef"))
print(Solution().reorganizeString("vvvlo"))
print(Solution().reorganizeString("baaba"))

