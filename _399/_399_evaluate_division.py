"""
399. Evaluate Division

Equations are given in the format A / B = k,
where A and B are variables represented as strings,
and k is a real number (floating point number).

Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is:
vector<pair<string, string>> euqations, vector<double>& values, vector<pair<string, string>> query.
where equations.size() == values.size(),the values are positive.
this represents the equations.return vector<double>. .

The example above:
equations = [ ["a", "b"], ["b", "c"] ]. values = [2.0, 3.0].
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid.
You may assume that evaluating the queries will result in no division by zero,
and there is no contradiction.
"""
class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """

    	def seeker(a, b, path=[]):
    		# seeking the result of a/
    		#print "looking for :", a, "/ ", b
    		if a not in dct.keys() or b not in dct.keys():
    			#print "case 1"
    			return 0
    		if b in dct[a]:
    			#print "case 2: great!"
    			return dct[a][b]
    		elif b not in dct[a]:
    			#print "case 3: keep looking =>"
    			tmp = []
    			for c in dct[a].keys():
    				if c not in path:
    					if (seeker(c, b, path+[c])):
    						return dct[a][c]*(seeker(c, b, path+[c]))
    		else:
    			return 0

        dct = {}
        for i in xrange(len(equations)):
        	nums = equations[i]
        	div = float(values[i])
        	if nums[0] in dct.keys():
        		dct[nums[0]][nums[1]] = div
        	else:
        		dct[nums[0]] = {nums[0]:1, nums[1]:div}
        	if nums[1] in dct.keys():
        		dct[nums[1]][nums[0]] = 1.0/div
        	else:
        		dct[nums[1]] = {nums[1]:1, nums[0]:1.0/div}

        res = []
        for pair in query:
        	if seeker(pair[0], pair[1]):
        		res += seeker(pair[0], pair[1]),
        	else:
        		res += -1,

        #print res
        return [float(n) for n in res]
