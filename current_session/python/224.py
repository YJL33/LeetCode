class Solution:
    def calculate(self, s: str) -> int:
        # clairification
        # validity?
        # upperbound/lowerbound of digit?
        # 
        # idea
        # go through the string
        # maintain the number
        # if see +-, complete the calculations before the operator, and reset sign and number
        # if see '(', stash the previous sign and calculations and reset sign and number
        # if see ')', merge the current result with the previous stash
        #
        # tc: O(n) to go through whole array.
        # sc: O(h), h is the height of stack, worst case O(n)
        # 
        # dummy cases
        # (1+(4+5+2)-3)+(6+8)
        # 1+(4+5*2)-3
        # 1+(4*5-2)-3
        # 1+(4+5*(3+3)+2)+3
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in '+-':
                res += sign*num
                sign, num = [-1, 1][c == '+'], 0
            elif c == '(':
                stack += (res,sign),
                sign, res = 1, 0
            elif c == ')':
                # print(num,stack)
                prev_res, prev_sign = stack.pop()
                res += sign*num
                res *= prev_sign        # things inside bracket should * prev_sign
                res += prev_res
                num = 0

        return res + num*sign

print(Solution().calculate("(1+(4+5+2)-3)+(6+8)") == (1+(4+5+2)-3)+(6+8))
print(Solution().calculate("1-(5)") == 1-(5))
print(Solution().calculate("1+1+1+(1-1+1-1+1-1-1+1+1+1+1-1-1-1-1-1-1+1+1+1)+(1+1)+(1+(1+(1-1+1-1+1)+(1+1)+1)+1)") == 1+1+1+(1-1+1-1+1-1-1+1+1+1+1-1-1-1-1-1-1+1+1+1)+(1+1)+(1+(1+(1-1+1-1+1)+(1+1)+1)+1))