"""
see https://leetcode.com/problems/swap-adjacent-in-lr-string/
"""
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # R can only move right, and L can only go left, until meet each other
        rs, ls, re, le = [], [], [], []
        for i in range(len(start)):
            if start[i] == 'R':
                rs += i,
            elif start[i] == 'L':
                ls += i,
            if end[i] == 'R':
                re += i,
            elif end[i] =='L':
                le += i,

        if len(rs) != len(re) or len(ls) != len(le):
            return False

        # check their position
        # R and L can not move pass each other
        if len(rs) > 0:
            ls += len(start),
            nextL = 0
            for i in range(len(rs)):
                while ls[nextL] < rs[i]:
                    nextL += 1
                if rs[i] > re[i] or re[i] >= ls[nextL]:      # if it's moving left or moving pass next L
                    return False
            ls.pop()

        if len(ls) > 0:
            rs = [-1] + rs
            nextR = len(rs)-1
            for i in range(len(ls)-1, -1, -1):
                while rs[nextR] > ls[i]:
                    nextR -= 1
                if ls[i] < le[i] or le[i] <= rs[nextR]:      # if it's moving right or moving pass next R
                    return False

        return True

    def canTransform_2(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # the order should remain the same
        before, after = [], []
        for i in range(len(start)):
            if start[i] in 'RL':
                before += start[i],
            if end[i] in 'RL':
                after += end[i],

        # check the order
        if ''.join(before) != ''.join(after):
            return False

        # check the moves
        rs, ls = [], []
        for j in range(len(start)):
            if start[j] == 'R':
                rs += j,
            if end[j] == 'R':
                if len(rs) == 0:
                    return False
                else:
                    rs.pop()

        for k in range(len(start)-1, -1, -1):
            if start[k] == 'L':
                ls += k,
            if end[k] == 'L':
                if len(ls) == 0:
                    return False
                else:
                    ls.pop()
        return True

        
    def canTransform_TLE(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # use dfs
        visit = {}
        stack = [start]
        
        chk = ["X", "R", "L"]
        while chk:
            c = chk.pop()
            if start.count(c) != end.count(c):
                return False

        while stack:
            tmp = stack.pop()
            if tmp not in visit:
                if tmp == end:              # comparing itself costs O(n)
                    return True
                # flip all XL -> LX and add to stack
                for i in range(len(tmp)-1):
                    if tmp[i:i+2] == "XL":
                        new = tmp[:i] + "LX" + tmp[i+2:]
                        stack += new,
                        # print "1st", stack
                # flip all RX -> XR and add to stack
                for i in range(len(tmp)-1):
                    if tmp[i:i+2] == "RX":
                        new = tmp[:i] + "XR" + tmp[i+2:]
                        stack += new,
                        # print "2nd", stack
                visit[tmp] = True

        return False

# print(Solution().canTransform("LLR", "RRL"))
# print(Solution().canTransform("RX", "XR"))
# print(Solution().canTransform("XLRXXL", "XLXRXL"))
# print(Solution().canTransform("XLRXXLL", "XLXRLLX"))
# print(Solution().canTransform("XXRXXRXLXLXXRXRXLXXRXXLXXRXXLXXLXLRXLXRX","XRXRXLXLXXXRXRXXXLRLXXXXRXLXXXLXLXXXXRLR"))
print(Solution().canTransform("XRXXXLXXXR","XXRLXXXRXX"), "should be False")
print(Solution().canTransform("RLX","XLR"), "should be False")
