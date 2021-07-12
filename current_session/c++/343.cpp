#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
  int integerBreak(int n) {
    // observation, is it only using 2 and 3??
    if (n == 2) return 1;
    if (n == 3) return 2;
    if (n == 4) return 4;
    if (n == 5) return 6;
    if (n%3 == 0) return pow(3,n/3);
    if (n%3 == 1) return pow(3,(n-1)/3)*4/3;
    return pow(3,(n-2)/3)*2;
  }
};