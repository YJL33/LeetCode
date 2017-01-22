"""
423. Reconstruct Original Digits from English

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Easy

Given a non-empty string containing an out-of-order English representation of digits 0-9,
output the digits in ascending order.

Note:

    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits.
    That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.
"""
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cdct, num = {"z":0, "w":0, "x":0, "u":0, "g":0, "o":0, "h":0, "f":0, "s":0, "i":0}, [0 for _ in xrange(10)]

        for i in xrange(len(s)):
            if s[i] in cdct:
                cdct[s[i]] += 1
            else:
                cdct[s[i]] = 1

        # deal with 0, 2, 4, 6, 8
        num[0], num[2], num[4], num[6], num[8] = cdct["z"], cdct["w"], cdct["u"], cdct["x"], cdct["g"]
        cdct["o"] = cdct["o"]-num[0]
        cdct["o"] = cdct["o"]-num[2]
        cdct["f"], cdct["o"] = cdct["f"]-num[4], cdct["o"]-num[4]
        cdct["s"], cdct["i"] = cdct["s"]-num[6], cdct["i"]-num[6]
        cdct["i"], cdct["h"] = cdct["i"]-num[8], cdct["h"]-num[8]

        # deal with 1, 3, 5, 7
        num[1], num[3], num[5], num[7] = cdct["o"], cdct["h"], cdct["f"], cdct["s"]
        cdct["i"] -= num[5]
        # deal with 9
        num[9] = cdct["i"]

        res = ""
        for i in xrange(len(num)):
            res += str(i)*num[i]
        return res