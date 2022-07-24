class Solution:
    def calculate(self, s: str) -> int:

        def update(op, num):
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            elif op == '/':
                stack.append(int(stack.pop() / num))
            return
                
        stack = []
        num, op = 0, '+'
        
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in '+-*/)':
                update(op, num)
                num, op = 0, c
                if c == ')':
                    tmp = 0
                    while isinstance(stack[-1], int):
                        tmp += stack.pop()
                    update(stack.pop(), tmp)
            elif c == '(':
                stack.append(op)
                num, op = 0, '+'
        update(op, num)                         # update last num
        return sum(stack)