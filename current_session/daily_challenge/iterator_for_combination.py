import itertools
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        tmpList = [x for x in characters]
        tmpList.sort()
        chars = ''.join(tmpList)
        self.combs = [x for x in itertools.combinations(chars, combinationLength)]
        self.cur = 0

    def next(self) -> str:
        self.cur += 1
        return ''.join(self.combs[self.cur-1])

    def hasNext(self) -> bool:
        return len(self.combs) > self.cur

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()