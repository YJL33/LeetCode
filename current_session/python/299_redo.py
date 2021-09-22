# simply compare secret and guess to get 'A's
# use dictionary to handle B's
import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c1 = collections.defaultdict(int)
        a, b = 0, 0
        toCheck = []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                toCheck += i,
                c1[secret[i]] += 1
        
        for i in toCheck:
            if guess[i] in c1 and c1[guess[i]] > 0:
                b += 1
                c1[guess[i]] -= 1
        
        return str(a)+"A"+str(b)+"B"