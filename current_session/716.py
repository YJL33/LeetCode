"""
716
"""
from typing import List
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []         # (value, index of max from here)

    def push(self, x: int) -> None:
        if self.stack and x >= self.stack[self.stack[-1][1]][0]:
            i = len(self.stack)         # index of max
        else:
            i = self.stack[-1][1] if self.stack else 0
        self.stack.append((x, i))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[self.stack[-1][1]][0]

    def popMax(self) -> int:
        i = self.stack[-1][1]           # max index
        res = self.stack[i][0]
        newMax = self.stack[self.stack[i-1][1]][0] if i > 0 else -float('inf')
        # scan and update the whole stack
        # copy all values one step left
        for i in range(i, len(self.stack)-1):
            if self.stack[i+1][0] >= newMax:
                newMax = self.stack[i+1][0]
                self.stack[i] = (self.stack[i+1][0], i)
            else:
                self.stack[i] = (self.stack[i+1][0], self.stack[i-1][1])
        self.stack.pop()
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()