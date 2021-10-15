
class Solution:
    def reformatNumber(self, number: str) -> str:
        res = []
        cntOfNumber = 0
        for n in number:
            if n not in "0123456789":
                continue
            else:
                res.append(n)
                cntOfNumber += 1
                if cntOfNumber%3 == 0:
                    res.append("-")
        
        if cntOfNumber == 1:
            return "".join(res)
        elif cntOfNumber%3 == 1:
            return "".join(res[:-3]) + "-" + res[-3] + res[-1]
        elif cntOfNumber%3 == 2:
            return "".join(res)
        else:
            return "".join(res[:-1])

print(Solution().reformatNumber("123 4-567"))
print(Solution().reformatNumber("123 4-5678"))
print(Solution().reformatNumber("123456"))
print(Solution().reformatNumber("123456789"))
print(Solution().reformatNumber("12"))
print(Solution().reformatNumber("1"))
print(Solution().reformatNumber("--17-5 229 35-39475 "))
