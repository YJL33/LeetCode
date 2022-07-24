class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots = [0 for _ in range(maxNumbers)]
        self.empty = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        if len(self.empty) == 0:
            return -1
        else:
            x = self.empty.pop()
            # assert(self.slots[x] == 0)
            self.slots[x] = 1
            return x

    def check(self, number: int) -> bool:
        return number in self.empty    

    def release(self, number: int) -> None:
        # assert(self.slots[number] == 1)
        self.slots[number] = 0
        self.empty.add(number)
        return
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)