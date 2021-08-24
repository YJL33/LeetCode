class Solution:
    def shuffle(self, A, n):
        l, r = A[:n], A[n:]
        res = []
        for i in range(n):
            res.append(l[i])
            res.append(r[i])
        return res