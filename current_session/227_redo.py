"""
227
"""
class Solution:
    def calculate(self, s: str) -> int:
        n, sign, div = 0, 1, False
        st = []                         # in the end, sum the stack
        for i in range(len(s)):
            if s[i] in '0123456789':
                n = 10*n+int(s[i])
            elif s[i] in '+-*/':
                prev = sign*n
                if div:
                    prev, div = int(st.pop()/prev), False
                if s[i] == '+':
                    st.append(prev)
                    sign, n = 1, 0
                elif s[i] == '-':
                    st.append(prev)
                    sign, n = -1, 0
                elif s[i] == '*':           # put it with sign
                    sign, n = prev, 0
                else:
                    div = True
                    st.append(prev)
                    sign, n = 1, 0
        
        prev = sign*n
        if div: prev, div = int(st.pop()/prev), False
        st.append(prev)

        return sum(st)

print(Solution().calculate("3+2*2"))
print(Solution().calculate(" 3/2 "))
print(Solution().calculate(" 3+5 / 2 "))
print(Solution().calculate("0/1"))
