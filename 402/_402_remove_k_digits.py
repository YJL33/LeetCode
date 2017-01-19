"""
 402. Remove K Digits

    User Accepted: 2
    User Tried: 3
    Total Accepted: 2
    Total Submissions: 7
    Difficulty: Medium

Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Note:

    The length of num is less than 105 and will be >= k.
    The given num does not contain any leading zero.
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # Go through the digits from left to right,
        # remove previous digits if that makes the number smaller
        # (and if we still have to remove digits). 
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'

    def removeKdigits2(self, num, k):
        # k times remove the leftmost digit followed by a smaller digit (or remove the last digit).
        # Didn't think this would be fast enough, but it is :-)
        sub = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
        for _ in range(k):
            num = sub(lambda m: m.group()[1:], num, 1)
        return num.lstrip('0') or '0'

    def removeKdigits3(self, num, k):
        # Fail at testcase 26
        if k == 0: return num
        if k == len(num): return "0"

        minhead, headpos = 10, -1

        for i in xrange(k+1):
            if ord(num[i])-48 < minhead:
                minhead, headpos = ord(num[i])-48, i
            if minhead == 0:         # go deal with numbers to be removed
                break

        if k+1 == len(num):
            return num[headpos]
        elif headpos == 0:
            return num[0] + self.removeKdigits(num[1:], k)
        else:
            k -= headpos
            while num[headpos] == '0': headpos += 1
            return self.removeKdigits(num[headpos:], k)