
# 26 bit
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = []

        while columnNumber != 0:
            left = columnNumber%26
            columnNumber = columnNumber//26
            if left != 0:
                res.append(chr(left-1+ord('A')))
            else:
                res.append('Z')
                columnNumber -= 1
            # print('res:', res, left, columnNumber)
        
        return ''.join(res[::-1])
            

print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(2147483647))
