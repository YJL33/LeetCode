/*
 * @lc app=leetcode id=824 lang=cpp
 *
 * [824] Goat Latin
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  string toGoatLatin(string sentence) {
    // break the sentence into vector
    // process the words
    // put them back to sentence
    string output;
    string s;
    string vowels = "aeiou";
    int count = 0;
    sentence += ' ';
    for (auto c : sentence) {
      if (c == ' ') {
        char initial = s.at(0);
        // non-vowel
        if (initial != 'a' && initial != 'e' && initial != 'i' && initial != 'o' && initial != 'u' &&
        initial != 'A' && initial != 'E' && initial != 'I' && initial != 'O' && initial != 'U') {
          string tmp = "";
          for (int j = 1; j < s.size(); j++) {
            tmp += s.at(j);
          }
          tmp += s.at(0);
          s = tmp;
        }
        // processing
        s += "ma";
        string postfix = "a";
        int cnt = 0;
        while (cnt < count) {
          postfix += "a";
          cnt++;
        }
        s += postfix;
        s += " ";
        output += s;
        // reset
        s.clear();
        count++;
      } else {
        s += c;
      }
    }
    output.pop_back();
    return output;
  }
};
// @lc code=end

