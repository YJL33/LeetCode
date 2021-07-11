#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  bool isMatch(string s, string p) {
    // use DP
    // dp[i][j] is the solution of s[:i] + p[:j]
    // "" "*"
    // "aa" "a"
    // "aa" "a*"
    // "aa" "a."
    // "aa" "a."
    // "ab" "aa*"
    // "aab" "a*bc*"
    // 
    // dp[i][j] = (i-1 < len(s) && j-1 < len(j) && s[i-1] == p[j-1] && dp[i-2][j-2])   if p[j] not in "*."
    //          = (dp[i][j-2]) or (dp[i-1][j-1] and p[j-1]==s[i-1]) "*"
    //          = (dp[i-1][j-1])
    int m = s.size(), n = p.size();
    vector<vector<bool> > dp(m+1, vector<bool>(n+1, false));
    dp[0][0] = true;
    for (int i=0; i<m+1; i++) {
      for (int j=1; j<n+1; j++) {
        if (p[j-1] == '*') {
          dp[i][j] = (dp[i][j-2]) || (i && dp[i-1][j] && (s[i-1] == p[j-2] || p[j-2] == '.'));
        } else if (p[i-1] == '.') {
          dp[i][j] = i && dp[i-1][j-1];
        } else {
          dp[i][j] = i && dp[i-1][j-1] && s[i-1] == p[j-1];
        }
      }
    }
    return dp[m][n];
  }
};
int main() {
  Solution sol = Solution();
  // "" "s*"
  // "aa" "a"
  // "aa" "a*"
  // "aa" "a."
  // "aa" "aa"
  // "ab" "aa*"
  // "aab" "a*bc*"
  vector<string> s{ "","aa","aa","aa","aa","ab","aab" };
  vector<string> p{ "s*","a","a*","a.","aa","aa*","a*bc*" };
  // bool res = sol.isMatch("aa", "a*");
  for (int i=0; i<s.size(); i++) {
    cout<<s[i]<<"   "<<p[i];
    printf(" res : %s\n", sol.isMatch(s[i], p[i]) ? "true" : "false");
  }
  
  return 0;
}