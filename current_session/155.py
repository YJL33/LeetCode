class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ms = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.ms or self.ms[-1] >= x:
            self.ms.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.ms[-1]:
            self.ms.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.ms[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()