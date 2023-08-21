/*
 * @lc app=leetcode id=415 lang=cpp
 *
 * [415] Add Strings
 */

// @lc code=start

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  string addStrings(string num1, string num2) {
    int cur1 = num1.size()-1, cur2 = num2.size()-1;
    int carry = 0;
    string output = "";
    while (cur1 != -1 || cur2 != -1 || carry != 0) {
      int tmp = carry;
      if (cur1 != -1) tmp += (num1[cur1--] - '0');
      if (cur2 != -1) tmp += (num2[cur2--] - '0');
      carry = tmp/10;
      output += to_string(tmp%10);
    }
    reverse(output.begin(), output.end());
    return output;
  }
};
// @lc code=end

