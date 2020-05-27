"""
66. Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        add = 1

        while add >= 1:
            digits[i] += 1
            if digits[i] >= 10:
                digits[i] = 0
                i -= 1
                if i == -1:
                    add = 0
                    digits = [1] + digits
            else:
                add = 0
        return digits
