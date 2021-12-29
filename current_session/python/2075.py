class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # first, convert encoded text into grid
        # start from (0,0)
        # keep add (+1, +1)
        # if out of bound, go to next i
        if encodedText == "": return ""
        
        l = len(encodedText)//rows
        grid = [encodedText[i*l:(i+1)*l] for i in range(rows)]
        res = []
        for i in range(len(grid[0])):
            tmp = []
            pos = (0,i)
            while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                tmp.append(grid[pos[0]][pos[1]])
                pos = (pos[0]+1, pos[1]+1)
            res += tmp
        # ans = ''.join(res)
        while res[-1] == " ":
            res.pop()
        
        return "".join(res)