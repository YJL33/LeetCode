//125
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
  bool isPalindrome(string s) {
    for (int i = 0, j = s.size()-1; i<j; i++, j--) {
      while (!isalpha(s[i]) && i < j) i++;
      while (!isalpha(s[j]) && i < j) j--;
      if (toupper(s[i]) != toupper(s[j])) return false;
    }
    return true;
  }
};
int main() {
  Solution sol = Solution();

  bool res = sol.isPalindrome("A man, a plan, a canal: Panama");
  printf("res : %s\n", res ? "true" : "false");
  return 0;
}
