"""
see https://leetcode.com/problems/alphabet-board-path/
"""
class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        ans, prev = "", "a"
        
        for i in range(len(target)):
            ans += self.getPath(prev, target[i])
            prev = target[i]
        return ans

    # given character x and y, return the path
    def getPath(self, s, e):
        
        if s == e:
            return "!"

        res = ""
        n1, n2 = ord(s)-97, ord(e)-97
        r1, c1 = n1//5, n1%5
        r2, c2 = n2//5, n2%5
        
        # put UL before DR to handle 'z' position
        if r1 > r2:
            res += "U"*(r1-r2)
        if c1 > c2:
            res += "L"*(c1-c2)
        if r1 < r2:
            res += "D"*(r2-r1)
        if c1 < c2:
            res += "R"*(c2-c1)
        return res+"!"

print(Solution().alphabetBoardPath("leet"))
print(Solution().alphabetBoardPath("code"))