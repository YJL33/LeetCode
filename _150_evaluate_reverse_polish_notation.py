"""
150. Evaluate Reverse Polish Notation

    Total Accepted: 74095
    Total Submissions: 296662
    Difficulty: Medium

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for c in tokens:
            if c.isdigit():                     # a single digit number
                nums += int(c),

            elif len(c) > 1:                    # a number for sure
                num, isPos = 0, True
                for i in xrange(len(c)):
                    if c[i] in '0123456789':    # see the number
                        num = num*10 + int(c[i])
                    elif c[i] == '-':
                        isPos = False
                if isPos:
                    nums += num,
                else:
                    nums += -num,

            elif not c.isdigit():               # a operator
                n1 = nums.pop()
                n2 = nums.pop()
                if c == "-":
                    nums += n2-n1,
                elif c == "+":
                    nums += n2+n1,
                elif c == "*":
                    nums += n2*n1,
                else:
                    if n2//n1 < 0 and n2%n1 != 0:   # if negative
                        nums += (n2//n1+1),
                    else:
                        nums += (n2//n1),
        assert len(nums) == 1
        return nums[0]