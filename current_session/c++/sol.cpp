#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
    int trap(vector<int>& height) {
      vector<int> left;
      for (int i = 0; i < height.size(); ++i) {
        if (left.size() > 0) {
          left.push_back(max(left.back(), height[i]));
        } else {
          left.push_back(height[i]);
        }
      }
      vector<int> right;
      for (int i = height.size()-1; i >= 0; --i) {
        if (right.size() > 0) {
          right.push_back(max(right.back(), height[i]));
        } else {
          right.push_back(height[i]);
        }
      }
      reverse(right.begin(), right.end());
      int water = 0;
      for (int i = 1; i < height.size(); ++i) {
        water += min(left[i], right[i])-height[i];
      }
      return water;
    }
  };

// cp c++/42.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
int main() {
  vector<int>test1 = {0,1,0,2,1,0,1,3,2,1,2,1};
  vector<int>test2 = {4,2,0,3,2,5};
  cout << Solution().trap(test1) << " should be 6"<< endl;
  cout << Solution().trap(test2) << " should be 9"<< endl;
}