#include <iostream>
#include <string>

using namespace std;

// clang++ -std=c++17 c++/394.cpp -o 394 && ./394 -v
class Solution {
public:
  string decodeString(string s) {
    string res;
    int k = 0;
    int i = 0;
    while (i < s.size()) {
      if (isdigit(s[i])) {
        k = 10*k + stoi(s.substr(i, 1));
        i++;
      } else if (s[i] == '[') {
        int j = finder(i, s);   // position of closing bracket
        // e.g. 'aa3[bcd]aa
        // .     01234567     -> j=7, i=3, l=j-i-1
        int l = j-i-1;
        string substr = decodeString(s.substr(i+1, l));
        for (int add = 0; add < k; add++) {
          res += substr;
        }
        i = j+1;
        k = 0;
      } else {
        res = res + s[i];
        i++;
      }
      // cout << "res now:  " << res << endl;
    }
    return res;
  }

  int finder(int start, string s) {
    int j = start+1;
    int need = 1;
    while (need > 0 & j < s.size()) {
      if (s[j] == '[') {
        need++;
      } else if (s[j] == ']') {
        need--;
      }
      j++;
    }
    // cout << "start" << start << " end" << j-1 << endl;
    return j-1;
  }
};

int main() {
  string s1 = "3[a]2[bc]";
  string s2 = "3[a2[c]]";
  string s3 = "2[abc]3[cd]ef";
  string s4 = "abc3[cd]xyz";
  cout << Solution().decodeString(s1) << endl;
  cout << Solution().decodeString(s2) << endl;
  cout << Solution().decodeString(s3) << endl;
  cout << Solution().decodeString(s4) << endl;
}