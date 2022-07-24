# implementation of stack:
# each push/pop operation cost: O(logN)
# top/getMin: O(1)
# maintain the push order as well

class MinStack:
    def __init__(self):
        self.arr = []
        self.st = [float('-inf')]
        self.toRmv = set()

    def push(self, val:int)->None:
        self.arr.append(val)
        self.st.append(val)
        self._percUp()
        return

    # pop the last element in arr
    def pop(self)->None:
        n = self.arr.pop()
        self.toRmv.add(n)
        while len(self.st) >= 2 and self.st[1] in self.toRmv:
            self.st[1], self.st[-1] = self.st[-1], self.st[1]
            x = self.st.pop()
            self.toRmv.remove(x)
            self._percDown()
        return

    def top(self)->int:
        return self.arr[-1]

    def getMin(self)->int:
        # print('st:', self.st)
        return self.st[1]

    def _percUp(self)->None:
        # percolate up
        # while child < node: swap child and node
        b = len(self.st)-1
        a = b//2
        # print("before:", self.st)
        while a > 0 and self.st[b] < self.st[a]:
            self.st[b], self.st[a] = self.st[a], self.st[b]
            a, b = a//2, a
        # print("after: ", self.st)
        return

    def _percDown(self)->None:
        # percolate down
        # while smaller_child < node, swap node and smaller_child
        a = 1
        b = 2*a
        # print("before: ", self.st)
        if b+1 < len(self.st) and self.st[b] > self.st[b+1]: b += 1
        while b < len(self.st) and self.st[b] < self.st[a]:
            self.st[b], self.st[a] = self.st[a], self.st[b]
            a, b = b, 2*b
            if b+1 < len(self.st) and self.st[b] > self.st[b+1]: b += 1
        # print("after: ", self.st)
        return


ms = MinStack()
# ms.push(10)
# ms.push(4)
# ms.push(3)
# ms.push(2)
# ms.push(7)
# ms.push(9)
# ms.push(8)
# ms.push(1)
# ms.push(5)
# ms.push(6)
# ms.pop()
# print(ms.st)
# print(ms.arr)
ms.push(-2)
ms.push(0)
ms.push(-1)
print(ms.getMin())
print(ms.top())
ms.pop()
# print(ms.top())
print(ms.getMin())