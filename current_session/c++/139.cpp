#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

// clang++ -std=c++17 c++/139.cpp -o 139 && ./139 -v  
class Solution {
public:
  bool wordBreak(string s, vector<string>& wordDict) {
    set<string> wordSet;
    for (auto w: wordDict) {
      wordSet.insert(w);
    }

    if (wordSet.find(s) != wordSet.end()) {
      return true;
    }
    // use DP
    // initialize the DP
    int sl = s.size();
    bool dp[sl+1];
    for (int i = 0; i <= sl; ++i) {
      dp[i] = false;
    }
    dp[0] = true;

    // dp[a+b] is true if dp[a] and s[a+1:b] in wordSet
    for (int end = 1; end <= sl; ++end) {
      for (int start = 0; start < end; ++start) {
        int l = end-start;
        string tmp = s.substr(start, l);
        if (dp[start] && wordSet.find(tmp) != wordSet.end()) {
          dp[end] = true;
        }
      }
    }
    return dp[sl];
  }
};

int main() {
  string t1 = "leetcode";
  string t2 = "applepenapple";
  string t3 = "catsandog";
  vector<string> w1 = {"leet","code"};
  vector<string> w2 = {"apple","pen"};
  vector<string> w3 = {"cats","dog","sand","and","cat"};
  cout << Solution().wordBreak(t1, w1) << endl;
  cout << Solution().wordBreak(t2, w2) << endl;
  cout << Solution().wordBreak(t3, w3) << endl;
}