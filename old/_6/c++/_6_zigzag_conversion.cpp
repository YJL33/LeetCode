/* Copyright [2017] <YJLee>
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
*/
# include <iostream>
# include <string>
# include <vector>

using std::string;
using std::vector;
using std::cout;
using std::endl;

class Solution {
 public:
    string convert(string s, int numRows) {
        if (numRows <= 1 || numRows >= s.length()) return s;
        int row = 0, step = 1;
        std::vector<std::string> lines (numRows, "");
        for (int i = 0; i < s.length(); ++i) {
        // for (std::vector<std::string>::iterator it = lines.begin(); it != lines.end(); ++it) {
            lines.at(row) += s[i];
            if (row == 0) {
                step = 1;
            }
            if (row == numRows-1) {
                step = -1;
            }
            row += step;
        }
        std::string res = "";
        // for (int i = 0; i < numRows; ++i) {
            // std::cout << lines.at(i) << endl;
        // }
        for (int i = 0; i < numRows; ++i) {
            res += lines.at(i);
        }
        return res;
    }
};
// int main() {
//     Solution sol = Solution();
//     std::cout << sol.convert("paypalishiring", 3) << std::endl;
// }
