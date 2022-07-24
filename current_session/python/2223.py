class Solution:
    def sumScores(self, s: str) -> int:
        # z function (similar to manacher's algorithm)
        # see more at
        # https://leetcode.com/problems/sum-of-scores-of-built-strings/discuss/1906961/Python-z-funcion-solution-explained.
        # https://wangwilly.github.io/willywangkaa/2018/03/19/Algorithm-Z-%E6%BC%94%E7%AE%97%E6%B3%95/
        # https://cp-algorithms.com/string/z-function.html

        def get_z(s):
            n = len(s)
            z = [0]*n
            bst = 0
            for i in range(1, n):
                if i <= z[bst] + bst:
                    z[i] = min(z[bst]+bst-i, z[i-bst])
                while i+z[i] < n and s[z[i]] == s[i+z[i]]:
                    z[i] += 1
                if z[i]+i > z[bst]+bst:
                    bst = i
            return z

        return sum(get_z(s)) + len(s)
        
    def sumScores_suffix(self, s: str) -> int:
        # idea: naive approach O(N^2)
        # use suffix (TLE)

        # edge case:
        if len(set(s)) == 1:
            return (len(s))*(len(s)+1)//2
        
        substr = ""
        suffix = []
        for c in s[::-1]:
            substr = c+substr
            if c == s[0]:
                suffix.append(substr)
        suffix.sort()

        idx = suffix.index(s)
        l, r = idx-1, idx+1
        point = len(s)
        def count(w1, w2, limit):
            i = 0
            limit = min([len(w1), len(w2), limit])
            while i < limit and w1[i] == w2[i]:
                i += 1
            return i
        
        L1, L2 = len(s), len(s)
        while l >= 0:
            dp = count(suffix[l], suffix[l+1], L1)
            if dp == 0: break
            L1 = dp
            point += dp
            l -= 1
        while r < len(suffix):
            dp = count(suffix[r], suffix[r-1], L2)
            if dp == 0: break
            L2 = dp
            point += dp
            r += 1
        
        return point
        