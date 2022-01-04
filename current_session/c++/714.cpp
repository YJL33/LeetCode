#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int>& prices, int fee) {
    // use DP
    int buy = -1*prices[0], noBuy = 0;    // profit at day i
    for (int i = 0; i < prices.size(); ++i) {
      int tmp = buy;
      buy = max(buy, noBuy-prices[i]);
      noBuy = max(noBuy, tmp+prices[i]-fee);
    }
    return noBuy;
  }
};

// cp c++/714.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
int main() {
  vector<int>test1 = {1,3,2,8,4,9};
  vector<int>test2 = {1,3,7,5,10,3};
  cout << Solution().maxProfit(test1, 2) << " should be 8"<< endl;
  cout << Solution().maxProfit(test2, 3) << " should be 6"<< endl;
}