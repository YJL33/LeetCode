#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int wiggleMaxLength(vector<int>& nums) {
    // find the longest wiggle sequence
    // whenever it's increasing or decreasing -> leave the extreme value
    // status: 0=None, 1=increasing, -1=decreasing
    int status = 0;
    int prev = INT_MAX;
    int cnt = 0;
    for (int i = 0; i < nums.size(); ++i) {
      // check the status
      if (prev == INT_MAX) {
        prev = nums[i];
        cnt++;
      }
      if (status == 0) {
        if (prev != INT_MAX && nums[i] > prev) {
          status = 1;
          prev = nums[i];
          cnt++;
        } else if (prev != INT_MAX && nums[i] < prev) {
          status = -1;
          prev = nums[i];
          cnt++;
        }
      } else if ( (status == -1 && nums[i] > prev) || (status == 1 && nums[i] < prev) ) {
        status *= -1;
        cnt++;              // add the length of sequence
      }
      prev = nums[i];
    }
    return cnt;
  }
};

// clang++ -std=c++17 c++/376.cpp -o 376 && ./376 -v
int main() {
  vector<int> test1 = {1,7,4,9,2,5};
  vector<int> test2 = {1,17,5,10,13,15,10,5,16,8};
  vector<int> test3 = {1,1};
  vector<int> test4 = {1,2,3,4,5,4,3,2,1};
  cout << Solution().wiggleMaxLength(test1) << endl;
  cout << Solution().wiggleMaxLength(test2) << endl;
  cout << Solution().wiggleMaxLength(test3) << endl;
  cout << Solution().wiggleMaxLength(test4) << endl;
}