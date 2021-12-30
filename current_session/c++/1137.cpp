#include <iostream>

using namespace std;

class Solution {
public:
  int tribonacci(int n) {
    // check all ns
    // 0, 1, 1, 2, 4,
    int a = 0, b = 1, c = 1;
    if (n <= 1) return n;
    if (n == 2) return 1;
    int cnt = 3;
    while (cnt != n) {
      int tmp = a+b+c;
      a = b;
      b = c;
      c = tmp;
      cnt += 1;
    }
    return a+b+c;
  }
};

// clang++ -std=c++17 c++/1137.cpp -o 1137 && ./1137 -v
int main() {
  cout << Solution().tribonacci(4) << endl;
  cout << Solution().tribonacci(25) << endl;
}