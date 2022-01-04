#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxScoreSightseeingPair(vector<int>& values) {
    // sightseeing spot: v[i]+v[j]+i-j
    // optimum start: v[i]+i
    int optimalStart = values[0]+0;
    int maxScore = INT_MIN;
    for (int i = 1; i < values.size(); ++i) {
      maxScore = max(maxScore, values[i]-i+optimalStart);
      optimalStart = max(optimalStart, values[i]+i);
    }
    return maxScore;
  }
};

// clang++ -std=c++17 c++/1014.cpp -o 1014 && ./1014 -v
int main() {
  vector<int> test1 = {8,1,5,2,6};
  vector<int> test2 = {1,2};
  cout << Solution().maxScoreSightseeingPair(test1) << endl;
  cout << Solution().maxScoreSightseeingPair(test2) << endl;
}