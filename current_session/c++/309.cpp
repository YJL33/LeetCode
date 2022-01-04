#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int>& prices) {
    // after sell stock, next day can not buy stock
    // initial state
    // buy: profit of buying at day i
    // ownStock: profit of (already) holding a stock at day i
    // coolDown: profit of selling at day i-1
    // freeToBuy: profit of not owning stock and free to buy at day i

    int buy = -1*prices[0], ownStock = -1*prices[0], coolDown = INT_MIN, freeToBuy = 0;
    for (int i = 1; i < prices.size(); ++i) {
      int buy2 = max(buy, freeToBuy-prices[i]);
      int ownStock2 = max(ownStock, buy);           // already hold yesterday vs buy yesterday
      int coolDown2 = ownStock2+prices[i];          // sell today -> tomorrow CD
      int freeToBuy2 = max(coolDown, freeToBuy);    // just left CD vs already free to buy
      buy = buy2, ownStock = ownStock2, coolDown = coolDown2, freeToBuy = freeToBuy2;
      // cout << "DP:" << buy << " , " << ownStock << ", " << coolDown << " , " << freeToBuy << "   day:" << i << endl;
    }
    return max(freeToBuy, coolDown);
  }
};

// cp c++/309.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
int main() {
  vector<int>test1 = {1,2,3,0,2};
  vector<int>test2 = {1};
  cout << Solution().maxProfit(test1) << " should be 3"<< endl;
  cout << Solution().maxProfit(test2) << " should be 0"<< endl;
}