class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.n = 0
        self.cnt = 0

    def fix(self, idx: int) -> None:
        if not self.n&(1<<idx):
            self.n += (1<<idx)
            self.cnt += 1
        return

    def unfix(self, idx: int) -> None:
        if self.n&(1<<idx):
            self.n -= (1<<idx)
            self.cnt -= 1
        return

    def flip(self) -> None:
        x = (1<<self.size)-1
        self.n = x-self.n
        self.cnt = self.size-self.cnt
        return

    def all(self) -> bool:
        return (self.n+1) == (1<<self.size)

    def one(self) -> bool:
        return self.n != 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:        
        return (bin(self.n)[2:].zfill(self.size))[::-1]


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()