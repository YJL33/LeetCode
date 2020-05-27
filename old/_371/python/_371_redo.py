"""
 371. Sum of Two Integers

    Total Accepted: 56070
    Total Submissions: 109556
    Difficulty: Easy
    Contributors: Admin

Calculate the sum of two integers a and b,
but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if (b == 0):
            return a
        add, carry = a^b, (a&b)<<1
        return self.getSum(add, carry)

def main():
    print Solution().getSum(10,5)

if __name__ == '__main__':
    main()