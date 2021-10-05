#include <iostream>
#include <map>

using namespace std;

class Solution {
public:
  // top-down (recursive) solution
  map<int, int> mp = {};
  int climbStairs_topDown(int n) {
    // can climb 1 or 2 steps
    // use recursive
    if (n <= 3) return n;
    if mp.find(n) == mp.end() {
      mp[n] = climbStairs(n-1)+climbStairs(n-2) 
      return mp[n];
    }
    return mp[n];
  }

  // bottom-up solution
  int climbStairs_bottomUp(int n) {
    if (n <= 3) return n;
    int one = 2, two = 3, i = 4;
    while (i < n) {
      int tmp = two;
      two += one;
      one = tmp;
      i++;
    }
    return one+two;
  }
};