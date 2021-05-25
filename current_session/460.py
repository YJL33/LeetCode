from typing import List
class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = []                   # sort by count
        self.dict = {}                  # key: (val,cnt)

    def get(self, key: int) -> int:
        # check dict
        # if exist:
        # update order in arr (+1)
        # update cnt in dict
        # return val (dict[key][0])
        if key in self.dict:
            self._updateCnt(key)
            return self.dict[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check arr size
        # if removal is needed: pop(-1) -> arr.append((key,1))
        # update dict: remove x (say we x=pop(-1) earlier) and add key (dict[key] = (val,1))
        # if key existed:
        # update the order in arr (arr[x] = (arr[x][0],arr[x][1]+1))
        # update dict: (dict[key] = (val,cnt+1))
        # if not: simply add it
        if self.cap == 0:
            return
        if len(self.arr) == self.cap and key not in self.dict:
            xkey, xcnt = self.arr.pop()
            del self.dict[xkey]
        if key in self.dict:
            self._updateCnt(key, value)
        else:
            self.arr.append((key, 0))
            self.dict[key] = (value, 0)
            self._updateCnt(key)
        return    

    def _updateCnt(self, key, value=None):
        xval, xcnt = self.dict[key]
        self.dict[key] = (value if value else xval, xcnt+1)
        i = self.arr.index((key, xcnt))
        self.arr[i] = (key, xcnt+1)
        # bubble sort
        while i > 0 and self.arr[i][1] >= self.arr[i-1][1]:
            self.arr[i], self.arr[i-1] = self.arr[i-1], self.arr[i]
            i -= 1
        return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
c = LFUCache(10)
ops = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
# ["LFUCache"]
val = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
res = []
for i in range(len(ops)):
    if ops[i] == 'put':
        k, v = val[i]
        res += c.put(k, v),
    else:
        k = val[i][0]
        res += c.get(k),
ans = [None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
print(res)
# print(ans)
if res != ans:
    print('invalid ans')
    for i in range(len(res)):
        if res[i] != ans[i]:
            print('i:', i)
            print('ops and val:', ops[i], val[i])
            print('ans:', ans[i])
            print('res:', res[i])
