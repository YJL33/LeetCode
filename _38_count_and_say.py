"""
38. Count and Say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
class Solution(object):
    def __init__(self):
        self.num = ['1']

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return

        while len(self.num) < n:
            self.num.append(self.helper(self.num[-1]))

        return self.num[n-1]

    def helper(self, string):
        # return 1 -> 11, 21 -> 1211
        # print string
        if not string:
            return ''

        res = ''
        i = 0
        counter = 0
        while i < len(string):
            counter += 1
            if i+1 == len(string):
                res += str(counter) + string[i]
            elif string[i] != string[i+1]:
                res += str(counter) + string[i]
                counter = 0
            i += 1

        return res