"""
282. Expression Add Operators

    Total Accepted: 21547
    Total Submissions: 76672
    Difficulty: Hard
    Contributors: Admin

Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary) +, -, or * between the digits,
so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""
import itertools
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # reduce calculations by re-using temperatory results.
        # 1. first, generate separation of numbers. (until no more separations)
        # 2. use dfs to seek all ops, meanwhile temperatory results will be saved.
        
        result = []
        for i in xrange(len(num)):
            for seps in itertools.combinations(xrange(1,len(num)), i):
                n = self.separator(num, seps)       # e.g. "123" => [123]/[12,3]/[1,23]/[1,2,3]
                if n: self.dfs(n[1:], target, str(n[0]), [n[0]], result)
        return result

    def dfs(self, nbs, tgt, cand, stk, res):
        # seek for ops for target
        if not nbs:
            if sum(stk) == tgt: res += cand,
            return
        self.dfs(nbs[1:], tgt, cand+"*"+str(nbs[0]), stk[:-1]+[stk[-1]*nbs[0]], res)
        if len(stk) == 2: stk = [sum(stk)]
        self.dfs(nbs[1:], tgt, cand+"+"+str(nbs[0]), stk+[nbs[0]], res)
        self.dfs(nbs[1:], tgt, cand+"-"+str(nbs[0]), stk+[-nbs[0]], res)

    def separator(self, s, cuts):
        # separate original string into list of numbers
        cuts += len(s),
        ans, last = [], 0
        for c in cuts:
            if len(s[last:c]) > 1 and s[last:c][0] == '0': return False    # skip leading zero
            ans += int(s[last:c]),
            last = c
        return ans


    def addOperators_0(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # brute force: get all valid equations and calculate them => TLE
        if not num: return []
        ops, eqns = [ i for i in itertools.product("+-*_", repeat=len(num)-1)], []
        for op in ops:
            eqns += num[0],
            leadingNum = num[0]
            for j in xrange(len(op)):
                if op[j] != "_":            # add op
                    eqns[-1] += op[j]
                    leadingNum = -1         # reset leading number
                if leadingNum == '0':       # eliminate number beginning with zero
                    eqns.pop()
                    break
                eqns[-1] += num[j+1]        # add number
                if leadingNum == -1: leadingNum = eqns[-1][-1]

        ans = [eqn for eqn in eqns if eval(eqn) == target]      # turn equations into answer.
        return ans
