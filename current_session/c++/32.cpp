#include <iostream>
#include <string>
#include <stack>

using namespace std;

// use stack
// for each i
//  if s[i] == '(' => 
//    if there's a current_start:
//      add current_start into stack, and reset current_start
//    else:
//      simply add i
//  else => check stack
//    if stack is not empty:
//      j = stack.top
//      current_start = min(current_start, j)
//      maxSeen = max(maxSeen, i-current_start+1)
//    else: reset current_start

class Solution {
public:
  int longestValidParentheses(string s) {
    stack<int> st;
    int maxSeen=0;
    int currentStart=s.size();
    for (int i=0; i<s.size(); ++i) {
      if (s[i] == '(') {
        if (currentStart != s.size()) {
          st.push(currentStart);
          currentStart=s.size();
        } else {
          st.push(i);
        }
      } else {
        if (!st.empty()) {
          currentStart = min(currentStart, st.top());
          st.pop();
          maxSeen = max(maxSeen, i-currentStart+1);
        } else {
          currentStart = s.size();
        }
      }
    }
    return maxSeen;
  }
};

int main() {
  string ssss = "()()()()()()";
  string s2 = "(()";
  string s3 = ")()())";
  string s4 = "";
  string s5 = "()(()";
  cout << Solution().longestValidParentheses(ssss) << " == 12" << endl;
  cout << Solution().longestValidParentheses(s2) << " == 2" << endl;
  cout << Solution().longestValidParentheses(s3) << " == 4" << endl;
  cout << Solution().longestValidParentheses(s4) << " == 0" << endl;
  cout << Solution().longestValidParentheses(s5) << " == 2" << endl;
}