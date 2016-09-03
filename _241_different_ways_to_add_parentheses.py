"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators,
return all possible ts from computing all the different possible ways to group them.
The valid operators are +, - and *.

Example 1

Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2

Output: [0, 2]

Example 2

Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
"""
import operator
import re
class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', s)            # magical regular expression
        nums = map(int, tokens[::2])            # nums: an array, ops: a method (operator.xxx)
        ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
        def build(lo, hi):                      # top-down method
           if lo == hi:
               return [nums[lo]]
           return [ops[i](a, b)
                   for i in xrange(lo, hi)
                   for a in build(lo, i)
                   for b in build(i + 1, hi)]
        return build(0, len(nums)-1)

    def diffWaysToCompute2(self, s):
        if s.isdigit():
            return [int(s)]
        res = []
        for i in xrange(len(s)):
            if s[i] in "-+*":
                res1 = self.diffWaysToCompute2(s[:i])
                res2 = self.diffWaysToCompute2(s[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, s[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
