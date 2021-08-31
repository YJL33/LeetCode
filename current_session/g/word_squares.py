import collections
class Solution:
    def wordSquares(self, words):
        # prefix dictionary
        # key: prefix, val: set of words having such prefix
        pref, res = collections.defaultdict(set), []
        for w in words:
            for i in range(len(w)):
                pref[w[:i + 1]].add(w)
        # dfs
        def dfs(i, arr):
            if i == len(arr[0]):
                res.append(arr)
            else:
                for w in pref["".join(row[i] for row in arr)]:
                    dfs(i+1, arr+[w])
        # try each one as first row
        for w in words:
            dfs(1, [w])
        return res

print(Solution().wordSquares(["area","lead","wall","lady","ball"]))
