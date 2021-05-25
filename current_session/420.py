"""
420
"""
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        def required(s):
            upper = 1-any([a.isupper() for a in s])
            lower = 1-any([a.islower() for a in s])
            digit = 1-any([a.isdigit() for a in s])
            return sum([upper, lower, digit])
        
        def checkRpt():
            replace, one, two, i = 0, 0, 0, 0
            while i < len(password):
                L = 1
                while i+1 < len(password) and password[i+1]==password[i]:
                    i, L = i+1, L+1
                if L >= 3:
                    replace += L//3
                    if L%3 == 0: one += 1
                    if L%3 == 1: two += 2
                i += 1
            return replace, one, two
            
        if len(password) < 6:               # need only insertion or replacement
            return max(required(password), 6-len(password))
        
        elif 6 <= len(password) <= 20:      # need only replacement, depending on repeating length
            r, _, _ = checkRpt()
            return max(required(password), r)
        else:                               # need only replacement and deletion
            needDelete = len(password)-20
            r, one, two = checkRpt()
            # print('d,r,1,2:',needDelete, r, one, two)
            r -= min(needDelete, one)
            r -= min(max(needDelete-one,0), two) // 2
            r -= max(needDelete-one-two, 0) // 3    # can save one replacement by delete 3
            # print('d,r,1,2:',needDelete, r, one, two)

            return needDelete + max(required(password), r)

# print(Solution().strongPasswordChecker('aaB'))
# print(Solution().strongPasswordChecker('aaa'))
# print(Solution().strongPasswordChecker('aaaa'))
# print(Solution().strongPasswordChecker('....'))
# print(Solution().strongPasswordChecker('aaaaaaaaaaaaaaaaaaaa'))     # 20
# print(Solution().strongPasswordChecker('aaaaaaaaaaaaaaaaaaaaa'))    # 21
# print(Solution().strongPasswordChecker('aaaaaaaaaaaaaaaaaaaaaa'))   # 22 (mod1)
print(Solution().strongPasswordChecker("aaaabbaaabbaaa123456A"))
