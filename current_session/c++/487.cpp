#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int findMaxConsecutiveOnes(vector<int>& nums) {
    int maxSeen = 0;
    int currentLengthWithFlip = 0;
    int currentLengthWithNoFlip = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == 1) {
        currentLengthWithFlip++;
        currentLengthWithNoFlip++;
      } else {
        currentLengthWithFlip = currentLengthWithNoFlip+1;
        currentLengthWithNoFlip = 0;
      }
      int tmp = max(currentLengthWithFlip, currentLengthWithNoFlip);
      maxSeen = max(maxSeen, tmp);
    }
    return maxSeen;
  }
};

// clang++ -std=c++17 c++/487.cpp -o 487 && ./487 -v
int main() {
  vector<int> test1 = {1,1,1,1,0,1,1,1,1,0,1,0,1,0};
  cout << Solution().findMaxConsecutiveOnes(test1) << endl;
}