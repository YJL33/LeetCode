"""
https://leetcode.com/problems/design-browser-history/
"""
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.bstack = []    # older page at left side
        self.fstack = []    # reversed
        self.curr = homepage

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.bstack += self.curr,
        self.curr = url
        self.fstack = []
        return 

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.bstack:
            self.fstack += self.curr,
            self.curr = self.bstack.pop()
            steps -= 1
        return self.curr

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.fstack:
            self.bstack += self.curr,
            self.curr = self.fstack.pop()
            steps -= 1
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)