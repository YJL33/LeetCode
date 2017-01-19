"""
9. Palindrome Number

Determine whether an integer is a palindrome.
Do this without extra space.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # compare two digits from both end toward middle (145ms, 212ms)
        if x < 0: return False
        elif x <= 9: return True

        left, right = 10, 1
        while x >= left*10:
            left *= 10

        while left > right:
            if (x//left)%10 == (x//right)%10:
                left, right = left/10, right*10
            else:
                return False

        return True

    def isPalindrome(self, x):
        # reverse the number (152ms, 165ms)
        if x < 0: return False

        res, remains = 0, x
        while remains:
            res, remains = res*10+remains%10, remains//10
        return res == x