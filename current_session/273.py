"""
see https://leetcode.com/problems/integer-to-english-words/
"""
class Solution(object):
    def __init__(self):
        self.nums = {\
                0: "Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven",\
                8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen",\
                14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",\
                19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",\
                70:"Seventy", 80: "Eighty", 90:"Ninety"}

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 2^31-1 is about 10^9, billion
        if num == 0:
            return self.nums[num]

        b = num // 1000000000
        m = (num % 1000000000) // 1000000
        k = (num % 1000000) // 1000
        s = (num % 1000)

        # print(b,m,k,s)

        res = []

        if b != 0:
            tmp = self.convert(b)
            res += tmp,
            res += "Billion",

        if m != 0:
            tmp = self.convert(m)
            res += tmp,
            res += "Million",

        if k != 0:
            tmp = self.convert(k)
            res += tmp,
            res += "Thousand",

        if s != 0:
            res += self.convert(s),

        return ' '.join(res)

    def convert(self, n):
        if n <= 20:
            return self.convert10(n)

        res = []
        h = n // 100
        ts = n % 100
        t = (n % 100) // 10
        a = (n % 10)
        # print(h,t,a)
        if h > 0:
            res += self.convert10(h),
            res += 'Hundred',
        
        if ts <= 20 and ts != 0:
            res += self.convert10(ts),
        else:
            if t > 0:
                res += self.nums[10*t],

            if a > 0:
                res += self.convert10(a),

        # print(res)

        return ' '.join(res)

    def convert10(self, n):
        return self.nums[n]
        
print(Solution().numberToWords(123456789))