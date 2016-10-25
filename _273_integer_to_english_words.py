"""
 273. Integer to English Words

    Total Accepted: 23564
    Total Submissions: 114932
    Difficulty: Hard
    Contributors: Admin

Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hint:

Did you see a pattern in dividing the number into chunk of words?
For example, 123 and 123000.
Group the number by thousands (3 digits).
You can write a helper function that takes a number less than 1000 and convert that chunk to words.
There are many edge cases. What are some good test cases?
Does your code work with input such as 0? Or 1000010?
(middle chunk is zero and should not be printed out)
"""
class Solution(object):
    def __init__(self):
        self.tens = {0:'', 1:'', 2:'Hundred', 3:'Thousand', 6:'Million', 9:'Billion'}
        self.nums = {\
                0: "", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven",\
                8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen",\
                14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen",\
                19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",\
                70:"Seventy", 80: "Eighty", 90:"Ninety"}

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        i, res = 0, []
        while 10**(i+1) <= num: i += 1
        # print num, i
        # assert (10**i) <= num <= (10**(i+1))-1       

        while i > -1:
            if i in self.tens:
                if num < 1000:
                    res += self.hundsToLists(num, i)
                    i = -1
                else:
                    res += self.hundsToLists(num//(10**i), i)
                    res += self.tens[i],
                num, i = num%(10**i), i-1
            else: i -= 1
        return ' '.join([r for r in res if r != '']) or "Zero"

    def hundsToLists(self, n, od):
        lst = []
        if n >= 100:
            lst += [self.nums[(n//100)], self.tens[2]]          # put hundreds first if needed
            n -= (n//100)*100
        if n in self.nums: lst += self.nums[n],                 # simply look-up
        else: lst += [self.nums[(n//10)*10], self.nums[n%10]]   # decipher ten and one
        return lst