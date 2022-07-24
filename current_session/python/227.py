class Solution:
    def calculate(self, s: str) -> int:
        # clairification
        # validity?
        # upperbound/lowerbound of digit?
        # no brackets but only "+-*/"
        # 
        # idea
        # 
        # use an additional stack to store temperary calculations, and return sum(arr) at the end
        #
        # go through the string
        # maintain the number
        # if see +-, complete the calculations before the operator, put it into stack, and reset sign and number
        # if see */,
        #
        # tc: O(n) to go through whole array.
        # sc: O(h), h is the height of stack, worst case O(n)
        # 
        # dummy cases
        # (1+(4+5+2)-3)+(6+8)
        # 1+(4+5*2)-3
        # 1+(4*5-2)-3
        # 1+(4+5*(3+3)+2)+3
        num, sign, div, st = 0, 1, False, []      # in the end, sum the stack
                                        
        for c in s:
            if c.isdigit():
                num = 10*num+int(c)
            elif c in '+-*/':
                prev = sign*num
                if div:
                    prev, div = int(st.pop()/prev), False
                if c in '+-':
                    st.append(prev)
                    sign, num = [-1,1][c =='+'], 0
                elif c == '*':                  # put it with sign
                    sign, num = prev, 0
                else:
                    div = True
                    st.append(prev)
                    sign, num = 1, 0
        
        prev = sign*num
        if div: prev, div = int(st.pop()/prev), False
        st.append(prev)

        return sum(st)

print(Solution().calculate("3+2*2"))
print(Solution().calculate(" 3/2 "))
print(Solution().calculate(" 3+5 / 2 "))
print(Solution().calculate("0/1"))