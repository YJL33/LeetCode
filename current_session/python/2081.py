class Solution:
    def __init__(self) -> None:
        self.base10s, self.tens = self.getBase10s()
        self.ans = []

    def kMirror(self, k: int, n: int) -> int:
        # check both base-10 and base-k
        # however, base-10 should be easier (and will be used in all cases)
        # 1. generate the common base-10 list
        # 2. for each of them, check whether its base-k

        def finder(arr):
            for x in arr:
                if self.isMirrorBaseK(x, k):
                    self.ans += x,
                if len(self.ans) == n: return True
            return False
        
        if finder(self.base10s): return sum(self.ans)
        
        eleven = self.getNext(self.tens, 100000, False)
        if finder(eleven): return sum(self.ans)

        twelve = self.getNext(self.tens, 100000, True)
        if finder(twelve): return sum(self.ans)

        thirteen = self.getNext(twelve, 1000000, False)
        if finder(thirteen): return sum(self.ans)

        fourteen = self.getNext(twelve, 1000000, True)
        if finder(fourteen): return sum(self.ans)

        print('need mor base10s')
        return -1
    
    def isMirrorBaseK(self, x, k):
        val = x
        res = []
        while val != 0:
            res.append(val%k)
            val = val//k
        l, r = 0, len(res)-1
        while l < r:
            if res[l] != res[r]: return False
            l, r = l+1, r-1
        return True

    def getNext(self, prevEven, div, isEven):
        p, q = 100 if isEven else 10, 11 if isEven else 1
        res = []
        for x in prevEven:
            a = x%div
            b = x-a
            res += [p*b+q*div*c+a for c in range(10)]
        return res

    def getBase10s(self):
        res = [a for a in range(1,10)]+[11*a for a in range(1,10)]
        three = [101*a+10*b for a in range(1,10) for b in range(10)]
        four = [1001*a+110*b for a in range(1,10) for b in range(10)]

        res += three
        res += four

        six = self.getNext(four, 100, True)
        res += self.getNext(four, 100, False)+six

        eight = self.getNext(six, 1000, True)        
        res += self.getNext(six, 1000, False)+eight

        ten = self.getNext(eight, 10000, True)   
        res += self.getNext(eight, 10000, False)+ten

        return res, ten

# print(Solution().kMirror(2,5))
# print(Solution().kMirror(3,7))
# print(Solution().kMirror(7,17))
print(Solution().kMirror(4,30))