#include <iostream>
#include <vector>
#include <set>

using namespace std;

// DP
// dp[n] = (x)+y for all x+y=n-1
class Solution {
public:
    vector<string> generateParenthesis(int n) {
      if (n == 1) return vector<string>{"()"};
      // use dp
      vector<vector<string> > dp;
      dp.push_back(vector<string>{""});
      dp.push_back(vector<string>{"()"});
      for (int i=2; i<=n; i++) {
        // carefully generate x and y
        vector<string> tmp;
        for (int a=0; a<i; ++a) {
          int b = i-a-1;
          for (auto x: dp[a]) {
            for (auto y: dp[b]) {
              tmp.push_back("("+x+")"+y);
            }
          }
        }
        dp.push_back(tmp);
      }

      return dp[n];
    }
};