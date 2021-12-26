import collections
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # use stack
        # check each element
        # if locked and '(': add as '('
        # if locked and ')': pop, see if can amend or not
        # if not locked: check the stack if it's possible to negate the previous one
        dq = collections.deque()
        i = 0
        while i < len(s):
            if locked[i] == '1' and s[i] == '(':
                dq.append((i, '('))
            elif locked[i] == '1' and s[i] == ')':
                if not dq: return False
                left, type = dq.pop()
            else:
                if dq[-1][1] == '(':
                    dq.pop()
                else:
                    dq.append((i, '_'))
            i += 1
        
        print('dq', dq)
        
        leftCnt = 0
        while dq:
            _, type = dq.popleft()
            if type == '(':
                leftCnt += 1
            else:
                if leftCnt:
                    leftCnt -= 1
                else:
                    leftCnt += 1

        return leftCnt == 0

print(Solution().canBeValid("())()))()(()(((())(()()))))((((()())(())","1011101100010001001011000000110010100101"), 'should be true')