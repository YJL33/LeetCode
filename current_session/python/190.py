class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = bin(n)[::-1][:-2]
        zeros = "0"*(32-len(reverse))
        return int('0b'+reverse+zeros, 2)