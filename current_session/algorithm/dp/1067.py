class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        
        # Think about the form of the number abcTxyz and the current digit T,
        # and we want to count the occurence of d on that position.
        # 1. If T>d, then from 000 to abc, each corresponds to 1000 counts
        # 2. If T==d, then from 000 to abc, each corresponds to 1000 counts except the last one,
        # and xyz correponds to a count of abcT000 to abcTxyz, which is xyz+1 counts.
        # 3. If T<d, then only from 000 to abc(excluded), each corresponds to 1000 counts.

        def getCounts(num):
            res, step, n = 0, 1, 0
            while num>0:
                t = num%10          # the current digit
                num = num//10       # the num in front of the digit
                if t>d:             # 
                    res += (1+num-(d==0))*step
                elif t==d:
                    res += (num-(d==0))*step+n+1
                else:
                    res += (num-(d==0))*step
                n += t*step         # update the number after the current digit
                step = 10*step      # update the weight
            return res
        
        return getCounts(high)-getCounts(low-1)

print(Solution().digitsCount(1,1,13))