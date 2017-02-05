/* Copyright [2017] <YJLee>
 12. Integer to Roman

    Total Accepted: 92222
    Total Submissions: 214117
    Difficulty: Medium
    Contributors: Admin

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
*/
# include <iostream>
# include <map>
# include <string>

using std::map;
using std::string;
using std::cout;
using std::endl;

class Solution {
 public:
    string intToRoman(int num) {
        std::map<int, char> roman = {{1, 'I'}, {5, 'V'}, {10, 'X'}, {50, 'L'},
                                    {100, 'C'}, {500, 'D'}, {1000, 'M'},
                                    {5000, 'Q'}};
        int divisor = 1000;
        std::string res;
        while (divisor != 0) {
            if (num/divisor == 4) {
                res += roman[divisor];
                res += roman[divisor*5];
            } else if (num/divisor == 9) {
                res += roman[divisor];
                res += roman[divisor*10];
            } else if (num/divisor >= 5) {
                res += roman[divisor*5];
                std::string tmp = std::string(num/divisor-5, roman[divisor]);
                res += tmp;
            } else if (num/divisor != 0) {
                std::string tmp = std::string(num/divisor, roman[divisor]);
                res += tmp;
            }
            num = num%divisor;
            divisor /= 10;
        }
        return res;
    }
};

int main() {
    Solution sol = Solution();
    std::cout << 2906 << " => "<< sol.intToRoman(2904) << endl;
    std::cout << 700 << " => "<< sol.intToRoman(700) << endl;
}
