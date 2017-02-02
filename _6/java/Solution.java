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
import java.util.*;

public class Solution {
    public String convert(String s, int numRows) {
        if (s.length() <= numRows || numRows < 2) return s;
        StringBuilder[] lines = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            lines[i] = new StringBuilder("");
        }
        int row = 0, step = 1;
        for (int j = 0; j < s.length(); j++) {
            lines[row].append(s.charAt(j));
            if (row == 0) step = 1;
            if (row == (numRows-1)) step = -1;
            row += step;
        }
        String res = "";
        for (int k = 0; k < numRows; k++) {
            res += lines[k];
        }
        return res;
    }
    // public static void main(String[] args) {
    //     Solution sol = new Solution();
    //     String word = "paypalishiring";
    //     System.out.println("Before: " + word);
    //     System.out.println("After: " + sol.convert(word, 3));
    //     return;
    // }
}
