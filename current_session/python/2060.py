from functools import cache
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        
        def gg(s): 
            """Return possible length."""
            ans = {int(s)}
            for i in range(1, len(s)): 
                ans |= {x+y for x in gg(s[:i]) for y in gg(s[i:])}
            return ans
        
        @cache
        def fn(i, j, diff): 
            """Return True if s1[i:] matches s2[j:] with given differences."""
            if i == len(s1) and j == len(s2): return diff == 0
            if i < len(s1) and s1[i].isdigit(): 
                ii = i
                while ii < len(s1) and s1[ii].isdigit(): ii += 1
                for x in gg(s1[i:ii]): 
                    if fn(ii, j, diff-x): return True 
            elif j < len(s2) and s2[j].isdigit(): 
                jj = j 
                while jj < len(s2) and s2[jj].isdigit(): jj += 1
                for x in gg(s2[j:jj]): 
                    if fn(i, jj, diff+x): return True 
            elif diff == 0: 
                if i < len(s1) and j < len(s2) and s1[i] == s2[j]: return fn(i+1, j+1, 0)
            elif diff > 0: 
                if i < len(s1): return fn(i+1, j, diff-1)
            else: 
                if j < len(s2): return fn(i, j+1, diff+1)
            return False 
            
        return fn(0, 0, 0)

print(Solution().possiblyEquals("internationalization", "i18n"), 't')
print(Solution().possiblyEquals("l123e", "44"), 't')
print(Solution().possiblyEquals("ab","a2"), 'f')
print(Solution().possiblyEquals("giejrqhftbrwnkqiwtnxcuggjaucanteswgpfmqq","1iejrqhftbrwnkqiwtnxcuggjaucanteswgpfmqq"), 't')
print(Solution().possiblyEquals("v853u344u9u8v838v726v78","v2v61v36v48u47v337v6v32"), 't')
print(Solution().possiblyEquals("a5b","c5b"), 'f')
print(Solution().possiblyEquals("98u8v8v8v89u888u998v88u98v88u9v99u989v8u","9v898u98v888v89v998u98v9v888u9v899v998u9"))