#include <iostream>
#include <vector>

using namespace std;


// cp c++/xxx.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
int main() {
  vector<int>test1 = {0};
  cout << Solution().xxx(test1) << " should be 1"<< endl;
}