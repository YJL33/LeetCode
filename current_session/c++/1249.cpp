#include <iostream>
#include <string>
#include <stack>

using namespace std;

class Solution {
public:
  string minRemoveToMakeValid(string s) {
    stack<int> st;
    // use stack, mark the invalid char as '#'
    for (int i=0; i<s.size(); ++i) {
      if (s[i] == '(') {
        st.push(i);
      } else if (s[i] == ')') {
        if (!st.empty()) {
          st.pop();
        } else {
          s[i] = '#';
        }
      }
    }
    while (!st.empty()) {
      s[st.top()] = '#';
      st.pop();
    }
    s.erase(remove(s.begin(), s.end(), '#'), s.end());
    return s;
  }
};