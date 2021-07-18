#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  string countAndSay(int n) {
    if (n == 1) return "1";
    return helper(countAndSay(n-1));
  }
private:
  string helper(string s) {
    string res;
    int prevI = 0;
    int cnt = 1;
    for (int i=1; i<s.size(); ++i) {
      if (s[i] == s[prevI]) {
        cnt += 1;
      } else {
        res = res + to_string(cnt) + s[prevI];
        cnt = 1;
        prevI = i;
      }
    }
    res = res + to_string(cnt) + s[prevI];
    return res;
  }

};