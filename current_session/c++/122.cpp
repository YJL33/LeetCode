#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int>& prices) {
    // use dp
    // buy and sell
    long buy= long(-prices[0]), sell = 0;
    for (int i=1; i<prices.size(); ++i) {
      int newBuy = max(buy, sell-prices[i]);
      int newSell = max(sell, buy+prices[i]);
      buy = newBuy;
      sell = newSell;
    }
    return sell;

  }
};