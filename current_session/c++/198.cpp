// clang++ -std=c++17 c++/198.cpp -o 198 && ./198 -v
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int rob(vector<int>& nums) {
    // use dp
    int rob = 0, notRob = 0;
    for (int i = 0; i < nums.size(); ++i) {
      int tmp = notRob + nums[i];
      notRob = max(rob, notRob);
      rob = tmp;
    }
    return max(rob, notRob);
  }
};

int main() {
  vector<int> test1 = {1,2,3,1};
  vector<int> test2 = {2,7,9,3,1};
  cout << Solution().rob(test1) << endl;
  cout << Solution().rob(test2) << endl;
}