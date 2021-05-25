"""
 155. Min Stack
Description Submission Solutions Add to List

    Total Accepted: 111930
    Total Submissions: 419333
    Difficulty: Easy
    Contributors: Admin

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack(object):
    """ use two stacks """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk += x,
        if len(self.minstk) == 0 or x <= self.minstk[-1]:
            self.minstk += x,
        return

    def pop(self):
        """
        :rtype: void
        """
        res = self.stk.pop()
        if res == self.minstk[-1]:
            return self.minstk.pop()
        return res

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()