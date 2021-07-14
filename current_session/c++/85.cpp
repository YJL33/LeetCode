#include <iostream>
#include <vector>
#include <stack>

using namespace std;
// naive approach:
// use dp to track each square dp[i][j] = f(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
// leverage histo
// O(NM)
class Solution {
public:
  int maximalRectangle(vector<vector<char>>& matrix) {
    vector<vector<int> > histo;
    for (int i=0; i<matrix.size(); ++i) {
      vector<int> tmp;
      for (int j=0; j<matrix[0].size(); ++j) {
        if (i==0) {
          matrix[i][j] == '0' ? tmp.push_back(0) : tmp.push_back(1);
        }
        else {
          matrix[i][j] == '0' ? tmp.push_back(0) : tmp.push_back(histo[i-1][j]+1);
        }
      }
      histo.push_back(tmp);
    }

    int maxSeen = 0;
    for (int i=0; i<histo.size(); ++i) {
      maxSeen = max(maxSeen, helper(histo[i]));
    }
    return maxSeen;
  }
private:
  int helper(vector<int> hist) {
    hist.push_back(0);
    stack<int> st;
    int zeroIndex = -1;
    int maxArea = 0;

    for (int i=0; i<hist.size(); ++i) {
      while (!st.empty() && hist[st.top()] < hist[i]) {
        int h = st.top(); st.pop();
        int prevI = st.empty() ? zeroIndex : st.top();
        int w = i-(prevI)+1;
        maxArea = max(maxArea, h*w);
      }
      st.push(i);
      if (hist[i] == 0) {
        st.pop();
        zeroIndex = i;
      }
    }
    return maxArea;
  }
};
