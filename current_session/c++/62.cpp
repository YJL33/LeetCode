#include <iostream>

using namespace std;

class Solution {
public:
  int uniquePaths(int m, int n) {
    long ans = 1;
    for(int i = m+n-2, j = 1; i >= max(m, n); i--, j++) 
        ans = (ans * i) / j;
    return ans;
  }
};

int main() {
  cout << Solution().uniquePaths(3,7) << endl;
  cout << Solution().uniquePaths(3,2) << endl;
}
