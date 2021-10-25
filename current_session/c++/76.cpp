#include <iostream>
#include <map>

using namespace std;

// clang++ -std=c++17 c++/76.cpp -o 76 && ./76 -v
class Solution {
public:
  string minWindow(string s, string t) {
    map<char, int> charCounter;
    
    for (int i = 0; i<t.size(); ++i) {
      charCounter[t[i]] += 1;
    }
    int l = 0, r = 0;
    int need = t.size();
    int minLen = INT_MAX;
    string res = "";
    bool checkSol = false;
    while (r < s.size()) {
      if (charCounter.find(s[r]) != charCounter.end()) {
        if (charCounter[s[r]] > 0) {
          need -= 1;
        }
        charCounter[s[r]] -= 1;

        while (need == 0) {
          checkSol = true;
          if (charCounter.find(s[l]) != charCounter.end()) {
            charCounter[s[l]] += 1;
            if (charCounter[s[l]] > 0) {
              need++;
            }
          }
          l++;
        }
        if (checkSol && charCounter.find(s[l-1]) != charCounter.end()) {
          int start = l-1, end = r;
          if (end-start < minLen) {
            res = s.substr(start, end-start+1);
            minLen = end-start;
          }
          checkSol = false;
        }
      }
      r++;
    }
    return res;
  }
};

int main() {
  cout << Solution().minWindow("aa", "aa") << endl;
  cout << Solution().minWindow("ADOBECODEBANC", "ABC") << endl;
  cout << Solution().minWindow("AA", "AA") << endl;
  cout << Solution().minWindow("A", "AA") << endl;
  cout << Solution().minWindow("ab","a") << endl;
  cout << Solution().minWindow("ab","b") << endl;
  cout << Solution().minWindow("cabwefgewcwaefgcf","cae") << " == cwae" << endl;
}