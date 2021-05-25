"""
see https://leetcode.com/problems/bulls-and-cows/
"""
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # bulls: digits in right pos
        # cows: digits in wrong pos
        # e.g. ABC -> ACB: 1A2B
        a, b = 0, 0
        cd = {}
        stack = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                a += 1
            else:
                # handle secret character and guess character
                sc, gc = secret[i], guess[i]
                if sc in cd:
                    cd[sc] += 1
                else:
                    cd[sc] = 1
                stack += (gc, i),
        while stack:
            c, i = stack.pop()
            if c in cd and cd[c] > 0:
                cd[c] -= 1
                b += 1

        return ''.join([str(a),'A',str(b),'B'])

print(Solution().getHint('1123','0111'))
print(Solution().getHint('1807','7810'))
print(Solution().getHint('1','0'))