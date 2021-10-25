// clang++ -std=c++17 c++/746.cpp -o 746 && ./746 -v 

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minCostClimbingStairs(vector<int>& cost) {
    if (cost.size() == 2) return min(cost[0], cost[1]);
    int a = 0, b = 0;
    for (int i = 2; i<=cost.size(); i++) {
      int tmp = min(a+cost[i-2], b+cost[i-1]);
      a = b;
      b = tmp;
    }
    return b;
  }
};

int main() {
  vector<int> test1 = {10,15,20};
  vector<int> test2 = {1,100,1,1,1,100,1,1,100,1};
  cout << Solution().minCostClimbingStairs(test1) << endl;
  cout << Solution().minCostClimbingStairs(test2) << endl;
}