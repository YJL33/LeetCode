"""
see https://leetcode.com/problems/partition-labels/
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        # 1. find the "span" of each character.
        # 2. check the span character(x) in S:
        #       for each character(y) within the span(X),
        #       check each span(Y) and update the major one(X)
        #       add len(X) into the result

        cd = {}
        for i in range(len(S)):
            c = S[i]
            if c in cd:
                l, r = cd[c]
                cd[c] = (l, i)
            else:
                cd[c] = (i, i)

        spans = []
        i = 0

        while i < len(S):
            l, r = cd[S[i]]
            tmpStk = []
            for c in S[l:r]:
                if c not in tmpStk:
                    tmpStk += c,

            while tmpStk:
                c = tmpStk.pop()
                cl, cr = cd[c]
                if cl < l:
                    for x in S[cl:l]:
                        if x not in tmpStk:
                            tmpStk += x,
                    l = cl
                if cr > r:
                    for x in S[r:cr]:
                        if x not in tmpStk:
                            tmpStk += x,
                    r = cr
            spans += len(S[l:r+1]),
            i = r+1

        # print(spans)
        return spans


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
