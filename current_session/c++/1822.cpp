#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int arraySign(vector<int>& nums) {
    int negativeCnt = 0;
    for (int i=0; i<nums.size(); ++i) {
      if (nums[i] == 0) return 0;
      if (nums[i] < 0) negativeCnt++;
    }
    return (negativeCnt%2 ? -1 : 1);
  }
};

int main() {
  int x;
  cin >> x;     // length of array
  vector<int> arr;
  while (x>0) {
    int a;
    cin >> a;
    arr.push_back(a);
    --x;
  }
  cout << "result: " << Solution().arraySign(arr) << endl;

}