"""
974
"""
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # use a smart way to handle the sum of subarray
        # sum(A[i:j]) = ps[j]-ps[i]

        # e.g.
        # A = [4,5,0,-2,-3,1]
        # ps = [0,4,9,9,7,4,5]
        # sum(A[1:2]) => A[1] = 5 => ps[2]-ps[1] = 9-4 = 5
        # sum(A[0:6]) => sum(A[0:6]) = 5 => ps[6]-ps[1] = 5-0 = 5

        ps, tmp = [0], 0
        for a in A:
            tmp += a
            ps += tmp,

        # check each i
        # store previous sub-sum in to dict
        cnt = 0
        mDict = {}
        mDict[0] = 1
        for i in range(1,len(ps)):
            mod = ps[i]%K               # sum(A[0:i]) == ps[i]-ps[0]
            if mod in mDict:
                cnt += mDict[mod]
                mDict[mod] += 1
            else:
                mDict[mod] = 1
        return cnt

    def subarraysDivByK_2(self, A, K):
        mDict = {}
        mDict[0], cnt, tmp = 1, 0, 0
        for a in A:
            tmp += a
            mod = tmp%K
            if mod in mDict:
                cnt += mDict[mod]
                mDict[mod] += 1
            else:
                mDict[mod] = 1

        return cnt

print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))
print(Solution().subarraysDivByK([1,1,1,3,4,6,1,3,7,6,-1,-3,-5,10,2,3,4,1], 5))