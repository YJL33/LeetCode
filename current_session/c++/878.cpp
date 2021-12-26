#include <iostream>
#include <algorithm>

using namespace std;

// clang++ -std=c++17 c++/878.cpp -o 878 && ./878 -v
class Solution {
public:
  int nthMagicalNumber(int n, int a, int b) {
    long l = min(a, b);
    long r = n*l;
    long lcm = (a*b)/__gcd(a,b);
    while (l < r) {
      m = l + (r-l)/2;
      if (m/a+m/b-m/lcm < n) {
        l = m+1;
      } else {
        r = m;
      }
    }
    return r%1000000007;
  }
};