/*
 344. Reverse String

    Total Accepted: 129550
    Total Submissions: 224187
    Difficulty: Easy
    Contributors: Admin

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
*/
# include <iostream>
# include <string>

using std::string;
using std::cout;
using std::endl;

class Solution {
 public:
    string reverseString(string s) {
        std::string res;
        for (int i = s.size()-1; i >= 0; i--) {
            res += s[i];
        }
        return res;
    }
};

int main() {
    std::cout << Solution().reverseString("Hello") << std::endl;
}