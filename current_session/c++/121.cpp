#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int>& prices) {
    int minPrice = prices[0];
    int maxProfit = 0;
    for (int i=1; i<prices.size(); ++i) {
      if (prices[i] < minPrice) {
        minPrice = prices[i];
      } else {
        maxProfit = max(prices[i]-minPrice, maxProfit);
      }
    }
    return maxProfit;
  }
};