"""
150
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(a-b)
                elif t == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            else:
                stack.append(int(t))

        return stack[-1]

print(Solution().evalRPN())