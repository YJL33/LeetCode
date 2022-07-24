class Solution:
    def isValid(self, s:str) -> bool:
        leftStack = []
        for i in range(len(s)):
            p = s[i]
            if p in "([{":
                leftStack.append(p)
            else:
                if not leftStack: return False
                l = leftStack[-1]
                if l == "(" and s[i] == ")":
                    leftStack.pop()
                elif l == "[" and s[i] == "]":
                    leftStack.pop()
                elif l == "{" and s[i] == "}":
                    leftStack.pop()
                else:
                    return False
        return False if leftStack else True

print(Solution().isValid("()"))
print(Solution().isValid("{[()]}{}"))
print(Solution().isValid("()[](]"))