# sliding Window
# remove edge cases First
# only find i when s1[i] = s2[0]
# reduce l into minimal l

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        # handle edge cases first
        if len(s2) > len(s1): return ""

        set1 = set(s1)
        for i in range(len(s2)):
            if s2[i] not in set1:
                return ""

        need = self.helper(s2)
        # keep increase r
        minWindow, i = "", 0
        while i < len(s1):
            if s1[i] == s2[0]:
                while s1[i+1:i+1+need] == s2[:need]: i += 1
                w = self.finder(s1[i:], s2)
                if w is not None and (not minWindow or len(w) < len(minWindow)):
                    minWindow = w
            i += 1
        return minWindow

    def helper(self, s):
        i = 0
        while i < len(s) and s[i] == s[0]:
            i += 1
        return i


    def finder(self, s, t):
        # print('given:', s, t)
        i, j = 0, 0
        while i < len(s) and j < len(t):
            # print('i, j', i, j)
            while i < len(s) and s[i] != t[j]:
                i += 1
            # now increment both i and j
            if i < len(s) and j < len(t) and s[i] == t[j]: j += 1
            i = i+1
        return s[:i] if j == len(t) else None