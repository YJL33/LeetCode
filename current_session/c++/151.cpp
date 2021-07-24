#include <iostream>
#include <string>
#include <stack>

using namespace std;

// put every word into a vector
// reverse the order of vector
class Solution {
public:
  string reverseWords(string s) {
    stack<string> st = helper(s);
    string ans;
    while (!st.empty()) {
      string w = st.top();
      st.pop();
      ans = ans + w;
      if (!st.empty()) ans += " ";
    }
    return ans;

  }
private:
  stack<string> helper(string s) {
    int i=0;
    stack<string> wordStack;
    while (i<s.size()) {
      if (s[i]!=' ') {
        int j=i+1;
        while (j<s.size() && s[j] != ' ') ++j;
        wordStack.push(s.substr(i, j-i));
        i = j;
      } else {
        ++i;
      }
    }
    
    return wordStack;
  }
};

int main() {
  string sss = "the sky is blue";
  cout << Solution().reverseWords(sss) << endl;
}