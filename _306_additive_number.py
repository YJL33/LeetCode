"""
306. Additive Number

    Total Accepted: 18983
    Total Submissions: 70048
    Difficulty: Medium
    Contributors: Admin

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.

1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros,
so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9',
write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""
import itertools
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        def seeker(i, j):                           # find valid A, B, and C => A + B = C
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)): return False       # eliminate leading zero
            while j < n:                            # keep matching as long as C is valid
                c = str(int(a)+int(b))
                if c == num[j:j+len(c)]:            # match C and original string
                    j, a, b = j+len(c), b, c        # match => update a & b
                else:
                    break                           # not match => C is invalid
            return (j == n)

        for p, q in itertools.combinations(range(1, n), 2):     # Try different initial condition
            if seeker(p, q): return True
        return False                                # Find nothing
