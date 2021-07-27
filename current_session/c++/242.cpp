#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return false;
    vector<int>sc(26, 0);
    vector<int>tc(26, 0);
    for (int i=0; i<s.size(); ++i) {
      sc[s[i]-'a'] += 1;
      tc[t[i]-'a'] += 1;
    }
    for (int j=0; j<sc.size(); ++j) {
      if (sc[j] != tc[j]) return false;
    }
    return true;
  }
};