"""
 6. ZigZag Conversion

    Total Accepted: 134045
    Total Submissions: 514716
    Difficulty: Medium
    Contributors: Admin

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    """Solution of Leetcode #6"""
    def convert(self, word, numofrows):
        """
        :type word: str
        :type numofrows: int
        :rtype: str
        """
        if numofrows <= 1 or numofrows >= len(word): return word
        line, row, step = ['' for _ in range(numofrows)], 0, 1
        for char in word:
            line[row] += char
            if row == 0:
                step = 1
            elif row == numofrows-1:
                step = -1
            row += step
        return ''.join(line)

# def main():
#     """ code here """
#     wordlist = ["abcdefghijkl", "a", "paypalishiring"]
#     norlist = [3, 10, 3]
#     print map(Solution().convert, wordlist, norlist)

# if __name__ == "__main__":
#     main()
