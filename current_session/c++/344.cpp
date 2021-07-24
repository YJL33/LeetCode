#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
  void reverseString(vector<char>& s) {
    int l=0, r=s.size()-1;
    while (l<r) {
      char tmp = s[r];
      s[r] = s[l];
      s[l] = tmp;
      l++;
      r--;
    }
    return;
  }
};