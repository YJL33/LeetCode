"""
 9. Palindrome Number

    Total Accepted: 179846
    Total Submissions: 528632
    Difficulty: Easy
    Contributors: Admin

Determine whether an integer is a palindrome.
Do this without extra space.
"""
class Solution(object):
    """Solution of leetcode #9"""
    def isPalindrome(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # reverse it then compare with original number
        if num < 0:
            return False
        res, origin = 0, num
        while num != 0:
            res, num = res*10+(num%10), num//10
            # print res, num
        return res == origin

def main():
    """code here"""
    print 1224, Solution().isPalindrome(1224)
    print 1221, Solution().isPalindrome(1221)

if __name__ == "__main__":
    main()
