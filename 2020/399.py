"""
399. Evaluate Division

Equations are given in the format A / B = k,
where A and B are variables represented as strings, and k is a real number
(floating point number).

Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is:
vector<pair<string, string>> equations,
vector<double>& values,
vector<pair<string, string>> queries,

where equations.size() == values.size(), and the values are positive.

This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid.

You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # naive aproach
        # phase 1
        # go through equations and values, establish a dictionary

        # phase 2
        # check all queries
        # make BFS for each query

        elementDict = {}
        for i in xrange(len(equations)):
            p, q = equations[i][0], equations[i][1]
            if p not in elementDict:
                elementDict[p] = {q: values[i]}
            else:
                elementDict[p][q] = values[i]
            if q not in elementDict:
                elementDict[q] = {p: 1/values[i]}
            else:
                elementDict[q][p] = 1/values[i]

        # print elementDict
        res = []
        for q in queries:
            a, b = q[0], q[1]
            # print "find:", a, b
            if a not in elementDict or b not in elementDict:
                res += -1.0,
            else:
                tmp = self.bfs(elementDict, a, b, [])
                res.append(tmp) if tmp != None else res.append(-1.0)

        return res


    def bfs(self, eDict, p, q, prev=[]):
        # print "p, q, prev", p, q, prev
        if p in prev:
            return
        if p == q:
            return 1.0
        if q not in eDict[p]:
            for x in eDict[p].keys():
                prev += p,
                tmp = self.bfs(eDict, x, q, prev)
                if tmp:
                    return eDict[p][x] * tmp
        else:
            return eDict[p][q]


# print Solution().calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])
# print Solution().calcEquation([["a","e"],["b","e"]],[4.0,3.0],[["a","b"],["e","e"],["x","x"]])
# print Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],[3.0,4.0,5.0,6.0],[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])
print Solution().calcEquation([["a","b"],["c","d"]],[1.0,1.0],[["a","c"],["b","d"],["b","a"],["d","c"]])
