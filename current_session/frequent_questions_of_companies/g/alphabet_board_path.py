# for each character, find the path
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        prev = 'a'
        for c in target:
            x = self.helper(prev, c)
            res.append(x)
            prev = c
        
        return ''.join(res)

    def helper(self, a, b):
        if a == b: return "!"
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z####"]
        ai, aj, bi, bj = None,None,None,None
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == a:
                    ai, aj = i, j
                elif board[i][j] == b:
                    bi, bj = i, j
        output = ""
        # U, L first, D, R later
        while ai > bi:
            output += "U"
            ai -= 1
        while aj > bj:
            output += "L"
            aj -= 1
        while ai < bi:
            output += "D"
            ai += 1
        while aj < bj:
            output += "R"
            aj += 1
        return output + "!"
print(Solution().alphabetBoardPath("leet"))
print(Solution().alphabetBoardPath("code"))
print(Solution().alphabetBoardPath("zdz"))